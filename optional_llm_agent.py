"""
Alternative LLM agent with offline/mock capabilities for testing.
Can work with or without API key.
"""
import json
import logging
from typing import Dict, Any, Optional
from config import EXTRACT_STRUCTURE_PROMPT

logger = logging.getLogger(__name__)


class MockLLMAgent:
    """Mock LLM agent for testing without API calls."""

    def __init__(self):
        """Initialize mock agent."""
        self.model = 'mock-gpt-3.5'
        logger.info("Using Mock LLM Agent (no API calls)")

    def analyze_website_structure(self, html_snippet: str) -> Dict[str, Any]:
        """Mock analysis - returns common selectors."""
        try:
            # Analyze HTML to find common patterns
            if 'product' in html_snippet.lower():
                if 'carrefour' in html_snippet.lower():
                    return {
                        'product_container': 'div[class*="products"]',
                        'product_item': 'article[class*="product"]',
                        'name_selector': 'h2[class*="name"]',
                        'price_selector': 'span[class*="price"]',
                        'discount_selector': 'span[class*="discount"]',
                        'unit_selector': 'span[class*="unit"]',
                        'quantity_selector': 'span[class*="qty"]'
                    }
                elif 'hyperone' in html_snippet.lower():
                    return {
                        'product_container': 'div.product-wrapper',
                        'product_item': 'div.product-item',
                        'name_selector': 'h3.product-title',
                        'price_selector': 'span.product-price',
                        'discount_selector': 'span.product-discount',
                        'unit_selector': 'span.product-unit',
                        'quantity_selector': 'span.product-quantity'
                    }
            
            # Default selectors
            return {
                'product_container': 'div[class*="product"]',
                'product_item': 'div[class*="item"], article[class*="product"]',
                'name_selector': 'h2, h3, [class*="name"]',
                'price_selector': '[class*="price"]',
                'discount_selector': '[class*="discount"]',
                'unit_selector': '[class*="unit"]',
                'quantity_selector': '[class*="quantity"]'
            }
        except Exception as e:
            logger.error(f"Error in mock analysis: {e}")
            return self._get_default_selectors()

    def extract_product_data(self, html_element: str) -> Dict[str, Any]:
        """Mock extraction - returns default structure."""
        return self._get_default_product_data()

    def validate_selectors(self, selectors: Dict[str, str], sample_html: str) -> bool:
        """Mock validation - always returns True."""
        return True

    @staticmethod
    def _get_default_selectors() -> Dict[str, str]:
        """Default selectors."""
        return {
            "product_item": "div[class*='product'], article",
            "name_selector": "h2, h3",
            "price_selector": "[class*='price']",
            "discount_selector": "[class*='discount']",
            "unit_selector": "[class*='unit']",
            "quantity_selector": "[class*='quantity']"
        }

    @staticmethod
    def _get_default_product_data() -> Dict[str, Any]:
        """Default product data."""
        return {
            "name": "Product",
            "price": 0.0,
            "discount": "",
            "unit": "",
            "quantity": 0
        }


class OptionalLLMAgent:
    """
    LLM agent that tries real API but falls back to mock if unavailable.
    Perfect for development and testing.
    """

    def __init__(self, use_mock: bool = False):
        """Initialize with fallback support."""
        self.use_mock = use_mock
        self.agent = None
        
        if use_mock:
            logger.info("Using Mock LLM Agent (as requested)")
            self.agent = MockLLMAgent()
        else:
            try:
                # Try to use real LLM agent
                from llm_agent import LLMAgent
                from google import genai
                from config import GEMINI_API_KEY
                
                if not GEMINI_API_KEY or GEMINI_API_KEY == 'your-key-here':
                    raise ValueError("Gemini API key not configured")
                
                genai.api_key = GEMINI_API_KEY
                self.agent = LLMAgent(GEMINI_API_KEY)
                logger.info("Using Real LLM Agent (genai)")
            except Exception as e:
                logger.warning(f"Cannot initialize real LLM agent: {e}")
                logger.info("Falling back to Mock LLM Agent")
                self.agent = MockLLMAgent()

    def analyze_website_structure(self, html_snippet: str) -> Dict[str, Any]:
        """Delegate to underlying agent."""
        return self.agent.analyze_website_structure(html_snippet)

    def extract_product_data(self, html_element: str) -> Dict[str, Any]:
        """Delegate to underlying agent."""
        return self.agent.extract_product_data(html_element)

    def validate_selectors(self, selectors: Dict[str, str], sample_html: str) -> bool:
        """Delegate to underlying agent."""
        return self.agent.validate_selectors(selectors, sample_html)

    def is_using_mock(self) -> bool:
        """Check if using mock agent."""
        return isinstance(self.agent, MockLLMAgent)
