"""Main runner script for the intelligent web scraper."""
import logging
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def setup_environment():
    """Set up environment and check dependencies."""
    logger.info("Setting up environment...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        logger.error("Python 3.8+ is required")
        sys.exit(1)
    
    # Create necessary directories
    for directory in ['output', 'cache', 'logs']:
        Path(directory).mkdir(exist_ok=True)
    
    logger.info("Environment setup complete")


def check_dependencies():
    """Check if all required packages are installed."""
    logger.info("Checking dependencies...")
    
    required_packages = [
        'scrapy',
        'openpyxl',
        'bs4',
        'selenium'
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    if missing:
        logger.error(f"Missing packages: {', '.join(missing)}")
        logger.error("Install with: pip install -r requirements.txt")
        return False
    
    logger.info("All dependencies installed")
    return True


def run_scraper(websites: list = None):

    logger.info("Starting intelligent web scraper...")

    try:

        from scrapy.crawler import CrawlerProcess
        from intelligent_spider import IntelligentProductSpider

        websites = [
            'https://www.hyperone.com.eg/ar/category/food-cupboard',
            'https://www.carrefour.com.eg/ar/'
        ]

        logger.info(f"Scraping websites: {websites}")

        custom_settings = {
            'BOT_NAME': 'intelligent-scraper',
            'SPIDER_MODULES': ['__main__'],
            'NEWSPIDER_MODULE': '__main__',

            'USER_AGENT': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 '
                '(KHTML, like Gecko) '
                'Chrome/148.0.7778.168 Safari/537.36'
            ),

            'ROBOTSTXT_OBEY': False,
            'CONCURRENT_REQUESTS': 8,
            'DOWNLOAD_DELAY': 2,
            'COOKIES_ENABLED': True,
            'RETRY_TIMES': 3,
            'LOG_LEVEL': 'INFO',
        }

        process = CrawlerProcess(custom_settings)

        process.crawl(
            IntelligentProductSpider,
            start_urls=websites
        )

        logger.info("Starting crawler...")

        process.start()

        logger.info("Scraper completed successfully!")

        return True

    except Exception as e:

        logger.error(f"Error running scraper: {e}")

        import traceback
        traceback.print_exc()

        return False

def test_llm_agent():
    """Test LLM agent functionality."""
    logger.info("Testing LLM agent...")
    
    try:
        from llm_agent import LLMAgent
        
        sample_html = """
        <div class="products">
            <div class="product-item">
                <h2 class="product-name">Sample Product</h2>
                <span class="price">99.99</span>
                <span class="discount">10%</span>
                <span class="unit">1kg</span>
                <span class="quantity">50</span>
            </div>
        </div>
        """
        
        agent = LLMAgent()
        logger.info("LLM Agent initialized successfully")
        
        # Note: Will need valid API key to actually test
        logger.warning("LLM Agent test requires valid Gemini API key in .env file")
        
    except Exception as e:
        logger.error(f"Error testing LLM agent: {e}")


def test_data_pipeline():
    """Test data pipeline."""
    logger.info("Testing data pipeline...")
    
    try:
        from data_pipeline import DataPipeline
        
        pipeline = DataPipeline()
        
        # Add sample items
        sample_items = [
            {
                'name': 'Apple',
                'price': 1.99,
                'discount': '10%',
                'unit': 'kg',
                'quantity': 100
            },
            {
                'name': 'Orange',
                'price': 2.49,
                'discount': '5%',
                'unit': 'kg',
                'quantity': 80
            }
        ]
        
        for item in sample_items:
            pipeline.process_item(item, 'test-site')
        
        # Export to Excel
        filepath = pipeline.export_to_excel()
        logger.info(f"Data pipeline test successful! Exported to: {filepath}")
        
        # Print statistics
        stats = pipeline.get_statistics()
        logger.info(f"Statistics: {stats}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error testing data pipeline: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main entry point."""
    logger.info("="*60)
    logger.info("Intelligent Web Scraper with LLM Agent")
    logger.info("="*60)
    
    # Setup and checks
    setup_environment()
    
    if not check_dependencies():
        logger.error("Dependency check failed. Please install requirements.txt")
        sys.exit(1)
    
    # Test components
    logger.info("\nRunning component tests...")
    test_data_pipeline()
    test_llm_agent()
    
    # Ask user what to do
    print("\n" + "="*60)
    print("Options:")
    print("1. Run full scraper (requires Gemini API key)")
    print("2. Test scraper with sample data (no API key needed)")
    print("3. Exit")
    print("="*60)
    
    choice = input("Select option (1-3): ").strip()
    
    if choice == '1':
        # Check for API key
        #client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

        #models = client.models.list()

        #for m in models:
        #    print(m.name)
        if not os.getenv('GEMINI_API_KEY'):
            logger.error("Gemini API key not found in .env file")
            logger.error("Create .env file with: GEMINI_API_KEY=your-key-here")
            sys.exit(1)
        
        websites = input("Enter websites to scrape (comma-separated, default: hyperone,carrefour): ").strip()
        if websites:
            websites = [w.strip() for w in websites.split(',')]
        else:
            websites = ['hyperone', 'carrefour']
        
        run_scraper(websites)
    
    elif choice == '2':
        logger.info("Running with sample data...")
        test_data_pipeline()
    
    else:
        logger.info("Exiting...")
        sys.exit(0)


if __name__ == '__main__':
    main()
