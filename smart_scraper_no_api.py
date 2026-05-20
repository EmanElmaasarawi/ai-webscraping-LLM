"""
Smart Web Scraper - NO API KEY NEEDED
Uses intelligent pattern matching instead of LLM
"""
import logging
import re
from typing import Optional, Dict, Any, List
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
import time

from data_pipeline import DataPipeline
from config import WEBSITES, COMMON_PATTERNS

logger = logging.getLogger(__name__)


class SmartProductScraper:
    """Smart scraper using pattern matching and heuristics - NO API NEEDED."""
    
    def __init__(self, website: str = 'hyperone'):
        """Initialize scraper for a specific website."""
        self.website = website
        self.website_config = WEBSITES.get(website)
        
        if not self.website_config:
            raise ValueError(f"Website {website} not configured")
        
        self.data_pipeline = DataPipeline()
        self.session = requests.Session()
        self.session.headers.update(self.website_config['headers'])
        
        logger.info(f"Initialized scraper for: {website}")

    def scrape_from_url(self, url: str) -> bool:
        """Scrape products from a specific URL."""
        logger.info(f"Scraping: {url}")
        
        try:
            # Fetch page
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract products
            products = self._extract_products_from_page(soup)
            
            if not products:
                logger.warning(f"No products found on {url}")
                return False
            
            # Process products through pipeline
            for product in products:
                self.data_pipeline.process_item(product, self.website)
            
            logger.info(f"Successfully extracted {len(products)} products")
            return True
            
        except Exception as e:
            logger.error(f"Error scraping {url}: {e}")
            return False

    def _extract_products_from_page(self, soup: BeautifulSoup) -> List[Dict[str, Any]]:
        """Extract all products from a page using intelligent pattern matching."""
        products = []
        
        selectors = self.website_config['selectors']
        
        # Find product containers
        product_items = soup.select(selectors['product_item'])
        logger.info(f"Found {len(product_items)} product items")
        
        for item in product_items:
            try:
                product = self._extract_single_product(item, selectors)
                if product and product.get('name') and product.get('price'):
                    products.append(product)
            except Exception as e:
                logger.debug(f"Error extracting product: {e}")
                continue
        
        return products

    def _extract_single_product(self, item, selectors: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """Extract data from a single product element."""
        try:
            product = {}
            
            # Extract name
            name = self._extract_text(item, selectors['name_selector'])
            if not name:
                return None
            product['name'] = name
            
            # Extract price
            price = self._extract_price(item, selectors['price_selector'])
            if not price:
                return None
            product['price'] = price
            
            # Extract discount (optional)
            product['discount'] = self._extract_text(
                item, 
                selectors['discount_selector']
            ) or "N/A"
            
            # Extract unit (optional)
            product['unit'] = self._extract_text(
                item,
                selectors['unit_selector']
            ) or "N/A"
            
            # Extract quantity (optional)
            quantity = self._extract_quantity(item, selectors['quantity_selector'])
            product['quantity'] = quantity
            
            return product
            
        except Exception as e:
            logger.debug(f"Error in product extraction: {e}")
            return None

    def _extract_text(self, element, selector: str) -> Optional[str]:
        """Extract and clean text from element."""
        try:
            if not selector:
                return None
            
            # Try the selector
            found = element.select_one(selector)
            if found:
                text = found.get_text(strip=True)
                return text if text else None
            
            return None
        except Exception as e:
            logger.debug(f"Error extracting text with selector '{selector}': {e}")
            return None

    def _extract_price(self, element, selector: str) -> Optional[float]:
        """Extract price from element."""
        try:
            text = self._extract_text(element, selector)
            if not text:
                return None
            
            # Extract numeric value
            # Remove common currency symbols and text
            cleaned = re.sub(r'[^\d.,]', '', text)
            cleaned = cleaned.replace(',', '.')
            
            # Handle multiple dots
            if cleaned.count('.') > 1:
                parts = cleaned.split('.')
                cleaned = parts[0] + '.' + parts[-1]
            
            try:
                return float(cleaned)
            except ValueError:
                return None
                
        except Exception as e:
            logger.debug(f"Error extracting price: {e}")
            return None

    def _extract_quantity(self, element, selector: str) -> int:
        """Extract quantity as integer."""
        try:
            text = self._extract_text(element, selector)
            if not text:
                return 0
            
            # Extract first number
            numbers = re.findall(r'\d+', text)
            return int(numbers[0]) if numbers else 0
            
        except Exception as e:
            logger.debug(f"Error extracting quantity: {e}")
            return 0

    def export_results(self) -> str:
        """Export collected data to Excel."""
        try:
            filepath = self.data_pipeline.export_to_excel()
            
            # Print statistics
            stats = self.data_pipeline.get_statistics()
            logger.info(f"\nScraped Statistics:")
            logger.info(f"  Total items: {stats['total_items']}")
            logger.info(f"  Valid items: {stats['valid_items']}")
            logger.info(f"  Invalid items: {stats['invalid_items']}")
            logger.info(f"  Exported to: {filepath}")
            
            return filepath
            
        except Exception as e:
            logger.error(f"Error exporting results: {e}")
            raise

    def get_statistics(self) -> Dict[str, Any]:
        """Get scraping statistics."""
        return self.data_pipeline.get_statistics()


class MultiSiteScraperNoAPI:
    """Scrape multiple websites without API key."""
    
    def __init__(self, websites: List[str] = None):
        """Initialize multi-site scraper."""
        if websites is None:
            websites = list(WEBSITES.keys())
        
        self.websites = websites
        self.scrapers = {}
        self.all_data = []
        
        # Create pipeline for all data
        self.pipeline = DataPipeline()

    def scrape_all(self) -> str:
        """Scrape all configured websites."""
        logger.info("Starting multi-site scraping (NO API KEY NEEDED)")
        
        for website in self.websites:
            try:
                logger.info(f"\nScraping: {website}")
                
                scraper = SmartProductScraper(website)
                url = WEBSITES[website]['url']
                
                if scraper.scrape_from_url(url):
                    # Merge data
                    for item in scraper.data_pipeline.data:
                        self.pipeline.data.append(item)
                        self.pipeline.stats['total_items'] += 1
                        self.pipeline.stats['valid_items'] += 1
                        self.pipeline.stats['websites_scraped'].add(website)
                
            except Exception as e:
                logger.error(f"Error scraping {website}: {e}")
                continue
        
        # Export all data
        return self.pipeline.export_to_excel()

    def add_custom_url(self, website_name: str, url: str) -> bool:
        """Scrape from a custom URL."""
        logger.info(f"Scraping custom URL: {url}")
        
        try:
            # Find closest website config
            base_website = next(iter(WEBSITES.keys()))
            config = WEBSITES[base_website]
            
            # Update headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            # Fetch and parse
            session = requests.Session()
            session.headers.update(headers)
            response = session.get(url, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Use generic selectors
            selectors = config['selectors']
            product_items = soup.select(selectors['product_item'])
            
            if not product_items:
                logger.warning("No products found")
                return False
            
            # Extract using SmartProductScraper logic
            scraper = SmartProductScraper(base_website)
            products = scraper._extract_products_from_page(soup)
            
            for product in products:
                self.pipeline.process_item(product, website_name)
            
            logger.info(f"Extracted {len(products)} products")
            return True
            
        except Exception as e:
            logger.error(f"Error scraping custom URL: {e}")
            return False

    def export_results(self) -> str:
        """Export all collected data."""
        return self.pipeline.export_to_excel()

    def get_statistics(self) -> Dict[str, Any]:
        """Get overall statistics."""
        return self.pipeline.get_statistics()
