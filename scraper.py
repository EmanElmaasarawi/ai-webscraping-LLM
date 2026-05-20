"""
Simple Web Scraper - NO API KEY NEEDED
Run this file to scrape websites
"""
import logging
import sys
from pathlib import Path

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def main():
    """Main entry point."""
    logger.info("=" * 80)
    logger.info("SMART WEB SCRAPER - NO API KEY NEEDED")
    logger.info("=" * 80)
    
    # Create output directories
    Path('output').mkdir(exist_ok=True)
    Path('cache').mkdir(exist_ok=True)
    
    print("\n" + "=" * 80)
    print("CHOOSE YOUR OPTION:")
    print("=" * 80)
    print("\n1. Scrape hyperone (Egyptian Hyperone)")
    print("2. Scrape carrefour (Carrefour Egypt)")
    print("3. Scrape BOTH")
    print("4. Scrape from custom URL")
    print("5. Exit")
    print("\n" + "=" * 80)
    
    choice = input("Enter your choice (1-5): ").strip()
    
    from smart_scraper_no_api import SmartProductScraper, MultiSiteScraperNoAPI
    
    if choice == '1':
        logger.info("Starting Hyperone scraper...")
        try:
            scraper = SmartProductScraper('hyperone')
            from config import WEBSITES
            url = WEBSITES['hyperone']['url']
            
            print(f"\nScraping from: {url}")
            print("Please wait...")
            
            if scraper.scrape_from_url(url):
                filepath = scraper.export_results()
                print(f"\n✓ Success!")
                print(f"  Excel file: {filepath}")
                stats = scraper.get_statistics()
                print(f"  Total products: {stats['valid_items']}")
            else:
                print("✗ No products found")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"✗ Error: {e}")
    
    elif choice == '2':
        logger.info("Starting Carrefour scraper...")
        try:
            scraper = SmartProductScraper('carrefour')
            from config import WEBSITES
            url = WEBSITES['carrefour']['url']
            
            print(f"\nScraping from: {url}")
            print("Please wait...")
            
            if scraper.scrape_from_url(url):
                filepath = scraper.export_results()
                print(f"\n✓ Success!")
                print(f"  Excel file: {filepath}")
                stats = scraper.get_statistics()
                print(f"  Total products: {stats['valid_items']}")
            else:
                print("✗ No products found")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"✗ Error: {e}")
    
    elif choice == '3':
        logger.info("Starting multi-site scraper...")
        try:
            print("\nScraping both websites...")
            print("This may take a minute, please wait...")
            
            scraper = MultiSiteScraperNoAPI(['hyperone', 'carrefour'])
            filepath = scraper.scrape_all()
            
            print(f"\n✓ Success!")
            print(f"  Excel file: {filepath}")
            stats = scraper.get_statistics()
            print(f"  Total products: {stats['valid_items']}")
            print(f"  Websites: {', '.join(stats['websites'])}")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"✗ Error: {e}")
    
    elif choice == '4':
        print("\n" + "=" * 80)
        url = input("Enter website URL (e.g., https://example.com/products): ").strip()
        website_name = input("Enter website name (e.g., MyStore): ").strip()
        
        if not url or not website_name:
            print("✗ Invalid input")
            return
        
        logger.info(f"Starting custom URL scraper: {url}")
        try:
            print(f"\nScraping from: {url}")
            print("Please wait...")
            
            scraper = MultiSiteScraperNoAPI()
            if scraper.add_custom_url(website_name, url):
                filepath = scraper.export_results()
                print(f"\n✓ Success!")
                print(f"  Excel file: {filepath}")
                stats = scraper.get_statistics()
                print(f"  Total products: {stats['valid_items']}")
            else:
                print("✗ No products found")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"✗ Error: {e}")
    
    elif choice == '5':
        print("Exiting...")
        return
    
    else:
        print("✗ Invalid choice")
        return
    
    print("\n" + "=" * 80)
    print("Scraping completed!")
    print("Check: output/scraped_products.xlsx")
    print("=" * 80)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCancelled by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        print(f"✗ Fatal error: {e}")
        sys.exit(1)
