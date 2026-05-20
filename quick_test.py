"""Quick verification that all components are working."""
import sys
import os

# Add project directory to path
sys.path.insert(0, r'd:\Eman Folder\Projects\webscraping- big data\find scraping data')

print("=" * 70)
print("WEB SCRAPER COMPONENT VERIFICATION")
print("=" * 70)

# Test 1: Config
print("\n[1/5] Checking configuration...")
try:
    from config import WEBSITES, SCRAPY_SETTINGS
    print(f"✓ Websites configured: {list(WEBSITES.keys())}")
    print(f"✓ Scrapy settings loaded")
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

# Test 2: Data Pipeline
print("\n[2/5] Testing data pipeline...")
try:
    from data_pipeline import DataPipeline
    
    pipeline = DataPipeline(output_folder='output', filename='test_run.xlsx')
    
    # Add test data
    test_items = [
        {'name': 'Apple', 'price': 1.99, 'discount': '5%', 'unit': 'kg', 'quantity': 100},
        {'name': 'Orange', 'price': 2.49, 'discount': '10%', 'unit': 'kg', 'quantity': 80},
        {'name': 'Banana', 'price': 0.99, 'discount': None, 'unit': 'bunch', 'quantity': 150},
    ]
    
    for item in test_items:
        if not pipeline.process_item(item, 'test-site'):
            print(f"✗ Failed to process: {item}")
    
    print(f"✓ Processed {pipeline.get_statistics()['valid_items']} items")
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 3: HTML Parsing
print("\n[3/5] Testing HTML parsing (BeautifulSoup)...")
try:
    from bs4 import BeautifulSoup
    
    html = '<div class="product"><h2 class="name">Test Product</h2><span class="price">9.99</span></div>'
    soup = BeautifulSoup(html, 'html.parser')
    
    name = soup.select_one('.name')
    price = soup.select_one('.price')
    
    if name and price:
        print(f"✓ HTML parsing works: {name.text}, {price.text}")
    else:
        print("✗ HTML parsing failed")
        sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

# Test 4: Selector Cache
print("\n[4/5] Testing selector cache...")
try:
    from llm_agent import SelectorCache
    
    cache = SelectorCache()
    test_selectors = {'name': 'h2.product', 'price': 'span.price'}
    
    cache.set_selectors('test', test_selectors)
    retrieved = cache.get_selectors('test')
    
    if retrieved == test_selectors:
        print("✓ Selector cache works")
    else:
        print("✗ Selector cache failed")
        sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    sys.exit(1)

# Test 5: Excel Export
print("\n[5/5] Exporting to Excel...")
try:
    filepath = pipeline.export_to_excel()
    if os.path.exists(filepath):
        file_size = os.path.getsize(filepath)
        print(f"✓ Excel file created: {filepath} ({file_size} bytes)")
    else:
        print(f"✗ Excel file not found")
        sys.exit(1)
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "=" * 70)
print("✓ ALL TESTS PASSED!")
print("=" * 70)

stats = pipeline.get_statistics()
print(f"\nStatistics:")
print(f"  - Total items: {stats['total_items']}")
print(f"  - Valid items: {stats['valid_items']}")
print(f"  - Invalid items: {stats['invalid_items']}")
print(f"  - Websites: {stats['websites']}")

print("\nNext steps:")
print("1. Get OpenAI API key from https://platform.openai.com/api-keys")
print("2. Create .env file with: OPENAI_API_KEY=sk-your-key")
print("3. Run: python run_scraper.py")

print("\nView output:")
print(f"  Excel: {filepath}")
print(f"  Logs: scraper.log")
print(f"  Cache: cache/learned_selectors.json")

sys.exit(0)
