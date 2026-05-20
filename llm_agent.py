"""LLM Agent for intelligent HTML analysis and selector detection."""
import json
import logging
from typing import Dict, Any, Optional
from google import genai
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)


class LLMAgent:
    """LLM-based agent for analyzing HTML and detecting product information."""

    def __init__(self, api_key: str = os.getenv('GEMINI_API_KEY')):
        """Initialize LLM agent with Gemini API."""
        self.api_key = api_key
        genai.api_key = api_key
        self.model = "gemini-2.5-flash"

    def analyze_website_structure(self, html_snippet: str) -> Dict[str, Any]:
        """
        Analyze HTML to detect product structure and CSS selectors.
        
        Args:
            html_snippet: Sample HTML from the website
            
        Returns:
            Dictionary with detected selectors for product fields
        """
        try:

            soup = BeautifulSoup(html_snippet, "html.parser")

            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            clean_html = str(soup)
            EXTRACT_STRUCTURE_PROMPT = """You are a precise web scraping assistant.
                Extract structured data from the HTML.

                Return ONLY JSON array or object.

                Rules:
                - No extra text
                - No markdown
                - No comments
                - Clean text only
                - Deduplicate repeated values

                HTML:
                {html}
                """
            prompt = EXTRACT_STRUCTURE_PROMPT.format(html=clean_html[:5000])  # Limit input size
            
            response = genai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert HTML analyzer. Return valid JSON only."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=500
            )
            
            result_text = response.choices[0].message.content
            
            # Extract JSON from response
            try:
                selectors = json.loads(result_text)
            except json.JSONDecodeError:
                # Try to extract JSON if wrapped in markdown code blocks
                if '```json' in result_text:
                    selectors = json.loads(result_text.split('```json')[1].split('```')[0])
                else:
                    logger.error(f"Failed to parse LLM response: {result_text}")
                    selectors = self._get_default_selectors()
            
            logger.info(f"Detected selectors: {selectors}")
            return selectors
            
        except Exception as e:
            logger.error(f"Error analyzing website structure: {e}")
            return self._get_default_selectors()

    def extract_product_data(self, html_element: str) -> Dict[str, Any]:
        """
        Extract product data from HTML element using LLM.
        
        Args:
            html_element: HTML of a single product element
            
        Returns:
            Dictionary with extracted product information
        """
        try:
            EXTRACT_DATA_PROMPT = """
                You are a strict data extraction engine.

                Extract product information from HTML.

                IMPORTANT RULES:
                - Output MUST be valid JSON only
                - No commentary
                - No markdown
                - No extra keys outside schema
                - Use null if value not found

                Schema:
                {
                "product-name": string or null,
                "price": string or null,
                "currency": string or null,
                "quantity": string or null,
                "unit": string or null,
                "discount": string or null
                }

                HTML:
                {html}
                """
            

            soup = BeautifulSoup(html_element, "html.parser")

            for tag in soup(["script", "style", "noscript"]):
                tag.decompose()

            clean_html = str(soup)
            prompt = EXTRACT_DATA_PROMPT.format(html=clean_html[:3000])
            
            response = genai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a product data extractor. Return valid JSON only with the exact fields requested."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.2,
                max_tokens=300
            )
            
            result_text = response.choices[0].message.content
            
            # Extract JSON from response
            try:
                data = json.loads(result_text)
            except json.JSONDecodeError:
                if '```json' in result_text:
                    data = json.loads(result_text.split('```json')[1].split('```')[0])
                else:
                    logger.warning(f"Failed to parse product data: {result_text}")
                    data = self._get_default_product_data()
            
            return data
            
        except Exception as e:
            logger.error(f"Error extracting product data: {e}")
            return self._get_default_product_data()

    def validate_selectors(self, selectors: Dict[str, str], sample_html: str) -> bool:
        """
        Validate that detected selectors work on sample HTML.
        
        Args:
            selectors: Dictionary of CSS selectors
            sample_html: Sample HTML to test
            
        Returns:
            True if selectors are valid, False otherwise
        """
        
        try:
            soup = BeautifulSoup(sample_html, 'html.parser')
            
            # Test each selector
            for key, selector in selectors.items():
                if not selector or selector == 'N/A':
                    continue
                result = soup.select(selector)
                if not result:
                    logger.warning(f"Selector '{selector}' for {key} returned no results")
                    return False
            
            return True
        except Exception as e:
            logger.error(f"Error validating selectors: {e}")
            return False

    @staticmethod
    def _get_default_selectors() -> Dict[str, str]:
        """Get default/fallback selectors."""
        return {
            "product_container": "div[class*='product']",
            "product_item": "article, div[class*='item'], li[class*='product']",
            "name_selector": "h2, h3, [class*='name'], [class*='title']",
            "price_selector": "[class*='price'], span[class*='price']",
            "discount_selector": "[class*='discount'], [class*='sale'], span[class*='off']",
            "unit_selector": "[class*='unit'], span[class*='weight']",
            "quantity_selector": "[class*='quantity'], [class*='stock'], span[class*='available']"
        }

    @staticmethod
    def _get_default_product_data() -> Dict[str, Any]:
        """Get default/fallback product data structure."""
        return {
            "name": "N/A",
            "price": 0.0,
            "discount": "N/A",
            "unit": "N/A",
            "quantity": 0
        }


class SelectorCache:
    """Cache for learned website selectors to avoid repeated LLM calls."""

    def __init__(self, cache_file: str = 'cache/learned_selectors.json'):
        """Initialize selector cache."""
        self.cache_file = cache_file
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict[str, Dict[str, str]]:
        """Load cache from file."""
        try:
            import os
            if os.path.exists(self.cache_file):
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load selector cache: {e}")
        return {}

    def save_cache(self) -> None:
        """Save cache to file."""
        try:
            import os
            os.makedirs(os.path.dirname(self.cache_file), exist_ok=True)
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
            logger.info(f"Selector cache saved to {self.cache_file}")
        except Exception as e:
            logger.error(f"Failed to save selector cache: {e}")

    def get_selectors(self, website_domain: str) -> Optional[Dict[str, str]]:
        """Get cached selectors for a website."""
        return self.cache.get(website_domain)

    def set_selectors(self, website_domain: str, selectors: Dict[str, str]) -> None:
        """Cache selectors for a website."""
        self.cache[website_domain] = selectors
        self.save_cache()

    def clear_cache(self, website_domain: str = None) -> None:
        """Clear cache for a website or all websites."""
        if website_domain:
            self.cache.pop(website_domain, None)
        else:
            self.cache = {}
        self.save_cache()
