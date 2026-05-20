"""Configuration for web scraper - NO API KEY NEEDED."""
import os
from dotenv import load_dotenv

load_dotenv()

# ✅ NO API KEY NEEDED - Uses pattern matching and BeautifulSoup
USE_LLM = False  # Set to False to disable LLM

# Website Configurations with CSS Selectors
WEBSITES = {
    'hyperone': {
        'url': 'https://www.hyperone.com.eg/ar/category/food-cupboard',
        'name': 'Hyperone',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        'selectors': {
            'product_item': 'div.product, div[class*="product"], article[class*="product"]',
            'name_selector': 'h2, h3, [class*="name"], [class*="title"], span[class*="product-name"]',
            'price_selector': 'span[class*="price"], div[class*="price"], [class*="priceAmount"]',
            'discount_selector': '[class*="discount"], [class*="sale"], span[class*="off"], span[class*="percent"]',
            'unit_selector': '[class*="unit"], span[class*="weight"], span[class*="size"]',
            'quantity_selector': '[class*="quantity"], [class*="stock"], span[class*="available"], [class*="in-stock"]'
        }
    },
    'carrefour': {
        'url': 'https://www.carrefouregypt.com/mafegy/ar/c/FEGY1660000',
        'name': 'Carrefour',
        'headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        },
        'selectors': {
            'product_item': 'div.product, div[class*="product"], li[class*="product"], article[class*="item"]',
            'name_selector': 'h2, h3, [class*="name"], [class*="title"], span[class*="product-name"]',
            'price_selector': 'span[class*="price"], div[class*="price"], [class*="priceAmount"], span[class*="EGP"]',
            'discount_selector': '[class*="discount"], [class*="sale"], span[class*="off"], span[class*="percent"], [class*="promotion"]',
            'unit_selector': '[class*="unit"], span[class*="weight"], span[class*="size"], span[class*="per"]',
            'quantity_selector': '[class*="quantity"], [class*="stock"], span[class*="available"], [class*="in-stock"]'
        }
    }
}

# Scraper Settings
SCRAPY_SETTINGS = {
    'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'ROBOTSTXT_OBEY': False,
    'CONCURRENT_REQUESTS': 4,  # Lower for respect to servers
    'DOWNLOAD_DELAY': 2,  # Delay between requests
    'COOKIES_ENABLED': True,
    'RETRY_TIMES': 2,
    'TIMEOUT': 30,
}

# NO LLM PROMPTS NEEDED - Using direct CSS selectors and pattern matching

# Data Export
EXPORT_FOLDER = './output'
EXCEL_FILENAME = 'scraped_products.xlsx'

# Cache Settings
CACHE_FOLDER = './cache'
SELECTOR_CACHE_FILE = 'learned_selectors.json'

# Common Pattern Matchers (for auto-detection)
COMMON_PATTERNS = {
    'name_patterns': [
        'name', 'title', 'product-name', 'product_name', 
        'product-title', 'item-name', 'product-title', 'heading'
    ],
    'price_patterns': [
        'price', 'priceAmount', 'product-price', 'sale-price',
        'current-price', 'price-now', 'final-price', 'cost'
    ],
    'discount_patterns': [
        'discount', 'sale', 'percent', 'off', 'promotion',
        'special-price', 'reduced', 'saving'
    ],
    'unit_patterns': [
        'unit', 'weight', 'size', 'quantity-unit', 'per',
        'measurement', 'amount'
    ],
    'quantity_patterns': [
        'quantity', 'stock', 'available', 'in-stock',
        'qty', 'quantity-available', 'stock-qty'
    ]
}
