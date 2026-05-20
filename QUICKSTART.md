"""
SETUP AND QUICK START GUIDE

This is an intelligent web scraper with LLM-based adaptation.
Follow these steps to get started:

================== STEP 1: INSTALLATION ==================

1. Make sure Python 3.8+ is installed:
   python --version

2. Install dependencies:
   pip install -r requirements.txt

3. Verify installation (no API key needed):
   python demo_scraper.py

   This should create: output/demo_products.xlsx

================== STEP 2: GET API KEY (Optional for Full Features) ==================

1. Visit: https://platform.openai.com/api-keys
2. Create a new API key
3. Copy the key (starts with sk-)

================== STEP 3: CONFIGURE API KEY ==================

1. Copy .env.example to .env:
   cp .env.example .env

2. Edit .env and add your API key:
   OPENAI_API_KEY=sk-your-actual-key-here

   (If you don't have an API key, the scraper will use defaults)

================== STEP 4: READY TO SCRAPE ==================

RUN DEMO (no API key needed):
    python demo_scraper.py
    Creates: output/demo_products.xlsx

RUN FULL SCRAPER (needs API key):
    python run_scraper.py
    Then select option 1

QUICK TEST:
    python quick_test.py

FULL TESTS:
    python test_components.py

================== PROJECT STRUCTURE ==================

config.py                    - Configuration and website setup
llm_agent.py                - Real LLM agent (requires API key)
optional_llm_agent.py       - LLM agent with fallback to mock
intelligent_spider.py       - Main Scrapy spider
data_pipeline.py            - Data processing and Excel export
demo_scraper.py             - Demo with sample data
run_scraper.py              - Main runner script
quick_test.py               - Quick verification
test_components.py          - Full component tests

================== OUTPUTS ==================

output/
  ├── demo_products.xlsx       - Demo data (from demo_scraper.py)
  ├── scraped_products.xlsx    - Real scraped data
  └── test_run.xlsx            - Test output

cache/
  └── learned_selectors.json   - Learned CSS selectors (to avoid re-learning)

scraper.log                     - Detailed log file

================== KEY FEATURES ==================

✓ Intelligent HTML Analysis - LLM detects product structure
✓ Multi-Website Support - Works with hyperone, carrefour, etc.
✓ Adaptive Selectors - Learns CSS selectors for each site
✓ Data Extraction - Name, price, discount, unit, quantity
✓ Excel Export - Formatted with statistics
✓ Caching - Avoids repeated LLM calls
✓ Error Handling - Robust and fault-tolerant
✓ Pagination - Automatic page following

================== TROUBLESHOOTING ==================

ERROR: Missing packages
  → pip install -r requirements.txt

ERROR: OPENAI_API_KEY not found
  → Create .env file with your API key
  → OR use mock mode (demo_scraper.py works without key)

No data being extracted
  → Check website structure (might have changed)
  → Clear cache: delete cache/learned_selectors.json
  → Check scraper.log for errors

LLM Agent errors
  → Verify API key is valid and has credits
  → Check internet connection
  → Check API rate limits

================== NEXT STEPS ==================

1. Run demo to see system working:
   python demo_scraper.py

2. Check output file:
   output/demo_products.xlsx

3. Get API key for real scraping:
   https://platform.openai.com/api-keys

4. Configure .env file with your key

5. Run full scraper:
   python run_scraper.py

6. Customize websites in config.py to add more sources

================== SUPPORT ==================

For detailed information, see:
  - README.md: Full documentation
  - config.py: Configuration options
  - Test output logs for debugging

Questions? Check the README.md file!
"""

if __name__ == '__main__':
    print(__doc__)
