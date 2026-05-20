"""Demo web scraper with sample data - for testing and demonstration."""
import logging
from data_pipeline import DataPipeline
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def demo_scrape_hyperone():
    """Demo scraping from hyperone (simulated with sample data)."""
    logger.info("=" * 70)
    logger.info("DEMO: Scraping hyperone products")
    logger.info("=" * 70)
    
    # Sample data that would be extracted from hyperone
    hyperone_products = [
        {
            'name': 'Fresh Tomatoes',
            'price': 2.99,
            'discount': '15%',
            'unit': 'kg',
            'quantity': 150
        },
        {
            'name': 'Organic Bananas',
            'price': 1.49,
            'discount': None,
            'unit': 'bundle',
            'quantity': 200
        },
        {
            'name': 'Red Apples',
            'price': 3.49,
            'discount': '10%',
            'unit': '1.5kg',
            'quantity': 120
        },
        {
            'name': 'Orange Oranges',
            'price': 2.99,
            'discount': '5%',
            'unit': 'kg',
            'quantity': 90
        },
        {
            'name': 'Kiwi Fruit',
            'price': 4.99,
            'discount': '20%',
            'unit': 'pack',
            'quantity': 50
        },
        {
            'name': 'Fresh Lettuce',
            'price': 1.99,
            'discount': None,
            'unit': '400g',
            'quantity': 200
        },
    ]
    
    return hyperone_products


def demo_scrape_carrefour():
    """Demo scraping from carrefour (simulated with sample data)."""
    logger.info("=" * 70)
    logger.info("DEMO: Scraping carrefour products")
    logger.info("=" * 70)
    
    # Sample data that would be extracted from carrefour
    carrefour_products = [
        {
            'name': 'Whole Milk 1L',
            'price': 3.50,
            'discount': '5%',
            'unit': '1L',
            'quantity': 80
        },
        {
            'name': 'Cheddar Cheese',
            'price': 5.99,
            'discount': '10%',
            'unit': '250g',
            'quantity': 45
        },
        {
            'name': 'Brown Bread',
            'price': 2.25,
            'discount': None,
            'unit': '800g',
            'quantity': 120
        },
        {
            'name': 'Butter Unsalted',
            'price': 4.49,
            'discount': '15%',
            'unit': '250g',
            'quantity': 35
        },
        {
            'name': 'Eggs (Dozen)',
            'price': 3.99,
            'discount': '8%',
            'unit': '12 pieces',
            'quantity': 100
        },
        {
            'name': 'Greek Yogurt',
            'price': 4.99,
            'discount': None,
            'unit': '500g',
            'quantity': 60
        },
        {
            'name': 'Orange Juice',
            'price': 2.99,
            'discount': '12%',
            'unit': '1L',
            'quantity': 150
        },
        {
            'name': 'Pasta Premium',
            'price': 1.49,
            'discount': '6%',
            'unit': '500g',
            'quantity': 200
        },
    ]
    
    return carrefour_products


def run_demo():
    """Run demo scraping and export to Excel."""
    logger.info("\n" + "=" * 70)
    logger.info("INTELLIGENT WEB SCRAPER - DEMO MODE")
    logger.info("=" * 70)
    logger.info(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Create pipeline
    pipeline = DataPipeline(
        output_folder='output',
        filename='demo_products.xlsx'
    )
    
    # Get demo data
    logger.info("\nFetching demo data...")
    hyperone_data = demo_scrape_hyperone()
    carrefour_data = demo_scrape_carrefour()
    
    # Process hyperone data
    logger.info(f"\nProcessing {len(hyperone_data)} hyperone products...")
    for product in hyperone_data:
        if pipeline.process_item(product, 'hyperone'):
            logger.info(f"  ✓ {product['name']} - {product['price']} {product['unit']}")
    
    # Process carrefour data
    logger.info(f"\nProcessing {len(carrefour_data)} carrefour products...")
    for product in carrefour_data:
        if pipeline.process_item(product, 'carrefour'):
            logger.info(f"  ✓ {product['name']} - {product['price']} {product['unit']}")
    
    # Get statistics
    stats = pipeline.get_statistics()
    logger.info(f"\n{'=' * 70}")
    logger.info("SCRAPING STATISTICS")
    logger.info(f"{'=' * 70}")
    logger.info(f"Total items processed: {stats['total_items']}")
    logger.info(f"Valid items: {stats['valid_items']}")
    logger.info(f"Invalid items: {stats['invalid_items']}")
    logger.info(f"Websites scraped: {', '.join(stats['websites'])}")
    
    # Export to Excel
    logger.info(f"\nExporting to Excel...")
    try:
        filepath = pipeline.export_to_excel()
        logger.info(f"✓ Export successful!")
        logger.info(f"  File: {filepath}")
        
        import os
        if os.path.exists(filepath):
            file_size = os.path.getsize(filepath)
            logger.info(f"  Size: {file_size:,} bytes")
        
        logger.info(f"\n{'=' * 70}")
        logger.info("✓ DEMO COMPLETED SUCCESSFULLY!")
        logger.info(f"{'=' * 70}")
        logger.info(f"\nOpen the Excel file to view the results:")
        logger.info(f"  {filepath}")
        logger.info(f"\nNext steps:")
        logger.info(f"  1. Get OpenAI API key: https://platform.openai.com/api-keys")
        logger.info(f"  2. Create .env file with your API key")
        logger.info(f"  3. Run: python run_scraper.py")
        logger.info(f"  4. Real scraper will use LLM to adapt to any website design")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Export failed: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = run_demo()
    exit(0 if success else 1)
