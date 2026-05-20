"""
Quick Demo - Scrape Real Websites Without API Key
"""
import logging
from smart_scraper_no_api import SmartProductScraper, MultiSiteScraperNoAPI
from config import WEBSITES

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def demo_scrape_websites():
    """Demo scraping from real websites."""
    logger.info("=" * 80)
    logger.info("DEMO: Scraping Real Websites - NO API KEY NEEDED")
    logger.info("=" * 80)
    
    print("\nAvailable websites to scrape:")
    print("1. Hyperone Egypt")
    print("2. Carrefour Egypt")
    print("3. Both websites")
    print("\nStarting demo scraping from Hyperone...")
    
    try:
        # Scrape from the configured Egyptian URLs
        print("\n" + "-" * 80)
        print("Scraping: Hyperone Egypt")
        print(f"URL: {WEBSITES['hyperone']['url']}")
        print("-" * 80)
        
        scraper = SmartProductScraper('hyperone')
        url = WEBSITES['hyperone']['url']
        
        if scraper.scrape_from_url(url):
            filepath = scraper.export_results()
            stats = scraper.get_statistics()
            
            print(f"\n✓ Successfully scraped Hyperone!")
            print(f"  File: {filepath}")
            print(f"  Products found: {stats['valid_items']}")
            print(f"  Invalid items: {stats['invalid_items']}")
        else:
            print("✗ No products found on Hyperone")
        
        # Try Carrefour
        print("\n" + "-" * 80)
        print("Scraping: Carrefour Egypt")
        print(f"URL: {WEBSITES['carrefour']['url']}")
        print("-" * 80)
        
        scraper2 = SmartProductScraper('carrefour')
        url2 = WEBSITES['carrefour']['url']
        
        if scraper2.scrape_from_url(url2):
            # Merge data into one file
            for item in scraper2.data_pipeline.data:
                scraper.data_pipeline.data.append(item)
            
            filepath = scraper.export_results()
            stats = scraper.get_statistics()
            
            print(f"\n✓ Successfully scraped Carrefour!")
            print(f"  File: {filepath}")
            print(f"  Total products: {stats['valid_items']}")
        else:
            print("✗ No products found on Carrefour")
        
        print("\n" + "=" * 80)
        print("✓ DEMO COMPLETED!")
        print("=" * 80)
        print(f"\nCheck the output file: output/scraped_products.xlsx")
        
    except Exception as e:
        logger.error(f"Error in demo: {e}")
        print(f"✗ Error: {e}")


if __name__ == '__main__':
    demo_scrape_websites()
