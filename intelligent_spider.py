"""Intelligent Scrapy spider with LLM-based adaptation."""
import logging
import re
from typing import Optional, Dict, Any
from urllib.parse import urljoin, urlparse
import scrapy
from scrapy import Request
from bs4 import BeautifulSoup

from llm_agent import LLMAgent, SelectorCache
from data_pipeline import DataPipeline
from config import WEBSITES, SCRAPY_SETTINGS

logger = logging.getLogger(__name__)

class IntelligentProductSpider(scrapy.Spider):

    """Intelligent spider that adapts to different website designs using LLM."""

    name = "intelligent"

    def __init__(self, start_urls=None, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.start_urls = start_urls or []
        self.data_pipeline = []


    async def start(self):

        for url in self.start_urls:

            logger.info(f"Starting crawl: {url}")

            yield scrapy.Request(
                url=url,
                meta={"playwright": True, "url": url},
                headers=WEBSITES.get(urlparse(url).netloc, {}).get('headers', {}),
                callback=self.parse_listing,
                dont_filter=True,
                errback=self.errback_httpbin
            )

    def parse_listing(self, response):
        """Parse product listing page."""
        website = response.meta['url']
        
        logger.info(f"Parsing listing from {website}: {response.url}")
        
        # Get or learn selectors for this website
        selectors2 = self._get_selectors(website, response)
        selectors = self._get_selectors(website, response) or {
        "product_item": 
            [
                "div[class*='product']",
                "li.product",
                "[data-product]",
                "article"
            ]
        }
       
        if not selectors:
            logger.error(f"Could not determine selectors for {website}")
            return

        # Extract product items
        try:
            product_items = []
            for sel in [
                selectors.get("product_item"),
                "div[class*='product']",
                "[data-product]",
                "article"
            ]:
                if sel:
                    product_items = response.css(sel)
                    if product_items:
                        break

            for product_item in product_items:
                yield self.parse_product(product_item, website, selectors)
        
        except Exception as e:
            logger.error(f"Error parsing products on {website}: {e}")
        
        # Handle pagination
        yield from self._get_next_pages(response, website, selectors)

    def parse_product(self, selector, website: str, selectors: Dict[str, str]) -> Dict[str, Any]:
        """Parse individual product from selector."""
        try:
            # Extract HTML of the product element
            product_html = selector.get()
            
            # Use LLM to extract data if needed
            item = self._extract_product_data(product_html, selectors, selector)
            
            if item:
                # Process through pipeline
                self.data_pipeline.process_item(item, website)
                return item
        
        except Exception as e:
            logger.error(f"Error parsing product: {e}")
        
        return None

    def _extract_product_data(self, product_html: str, selectors: Dict[str, str], selector) -> Optional[Dict[str, Any]]:
        """Extract product data using both CSS selectors and LLM."""
        try:
            item = {}
            
            # Try to extract using detected selectors first
            if selectors.get('name_selector'):
                name = selector.css(selectors['name_selector']).get()
                if name:
                    item['name'] = BeautifulSoup(name, 'html.parser').get_text(strip=True)
            
            if selectors.get('price_selector'):
                price = selector.css(selectors['price_selector']).get()
                if price:
                    price_text = BeautifulSoup(price, 'html.parser').get_text(strip=True)
                    # Extract numeric value
                    price_match = re.search(r'[\d,.]+', price_text)
                    if price_match:
                        item['price'] = float(price_match.group().replace(',', '.'))
            
            if selectors.get('discount_selector'):
                discount = selector.css(selectors['discount_selector']).get()
                if discount:
                    item['discount'] = BeautifulSoup(discount, 'html.parser').get_text(strip=True)
            
            if selectors.get('unit_selector'):
                unit = selector.css(selectors['unit_selector']).get()
                if unit:
                    item['unit'] = BeautifulSoup(unit, 'html.parser').get_text(strip=True)
            
            if selectors.get('quantity_selector'):
                quantity = selector.css(selectors['quantity_selector']).get()
                if quantity:
                    quantity_text = BeautifulSoup(quantity, 'html.parser').get_text(strip=True)
                    quantity_match = re.search(r'\d+', quantity_text)
                    if quantity_match:
                        item['quantity'] = int(quantity_match.group())
            
            # If LLM didn't get all fields, use LLM agent
            if not all(k in item for k in ['name', 'price']):
                llm_data = self.llm_agent.extract_product_data(product_html)
                item.update(llm_data)
            
            # Ensure required fields
            if not item.get('name') or not item.get('price'):
                return None
            
            return item
        
        except Exception as e:
            logger.error(f"Error extracting product data: {e}")
            return None

    def _get_selectors(self, website: str, response) -> Optional[Dict[str, str]]:
        """Get or learn selectors for a website."""
        if website in self.learned_selectors:
            return self.learned_selectors[website]
        
        # Check cache
        cached = self.selector_cache.get_selectors(website)
        if cached:
            logger.info(f"Using cached selectors for {website}")
            self.learned_selectors[website] = cached
            return cached
        
        # Learn new selectors using LLM
        logger.info(f"Learning selectors for {website} using LLM...")
        
        try:
            # Get sample HTML
            sample_html = response.text[:8000]
            
            # Analyze with LLM
            selectors = self.llm_agent.analyze_website_structure(sample_html)
            
            # Validate selectors
            if self.llm_agent.validate_selectors(selectors, response.text):
                logger.info(f"Successfully learned selectors for {website}")
                self.selector_cache.set_selectors(website, selectors)
                self.learned_selectors[website] = selectors
                return selectors
            else:
                logger.warning(f"Validation failed for {website}, using defaults")
                # Fall back to defaults
                selectors = {
                    'product_item': 'div[class*="product"], article[class*="item"]',
                    'name_selector': 'h2, h3, [class*="name"]',
                    'price_selector': '[class*="price"]',
                    'discount_selector': '[class*="discount"], [class*="sale"]',
                    'unit_selector': '[class*="unit"], [class*="weight"]',
                    'quantity_selector': '[class*="quantity"], [class*="stock"]'
                }
                self.learned_selectors[website] = selectors
                return selectors
        
        except Exception as e:
            logger.error(f"Error learning selectors for {website}: {e}")
            return None

    def _get_next_pages(self, response, website: str, selectors: Dict[str, str]):
        """Get next pages for pagination."""
        try:
            # Try common pagination patterns
            next_page_patterns = [
                '//a[contains(@class, "next")]/@href',
                '//a[text()="Next"]/@href',
                '//a[contains(@href, "page")]/@href',
                '//li[@class="next"]/a/@href'
            ]
            
            for pattern in next_page_patterns:
                next_urls = response.xpath(pattern).getall()
                for next_url in next_urls[:3]:  # Limit to 3 pages
                    full_url = urljoin(response.url, next_url)
                    yield Request(
                        full_url,
                        callback=self.parse_listing,
                        meta=response.meta,
                        headers=WEBSITES[website]['headers'],
                        dont_obey_robotstxt=True
                    )
        
        except Exception as e:
            logger.warning(f"Error finding next page: {e}")

    def errback_httpbin(self, failure):
        """Handle request errors."""
        logger.error(f"Request failed: {failure.request.url} - {failure.value}")

    def closed(self, reason):
        """Called when spider is closed."""
        logger.info(f"Spider closed. Reason: {reason}")
        
        # Export data
        try:
            filepath = self.data_pipeline.export_to_excel()
            stats = self.data_pipeline.get_statistics()
            
            logger.info(f"Scraping completed!")
            logger.info(f"Statistics: {stats}")
            logger.info(f"Data exported to: {filepath}")
            
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
