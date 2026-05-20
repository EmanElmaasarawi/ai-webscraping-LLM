# Intelligent Web Scraper with LLM Agent

A professional web scraper that uses AI/LLM agents to automatically detect and adapt to different website designs. Extracts product information (name, price, discount, unit, quantity) and exports to Excel.

## Features

✓ **Intelligent Adaptation**: Uses LLM (GPT-3.5/GPT-4) to analyze HTML and automatically detect product structure  
✓ **Multi-Website Support**: Works with hyperone, carrefour, and other e-commerce sites  
✓ **Generic Selectors**: Learns CSS selectors for different website layouts  
✓ **Data Extraction**: Captures name, price, discount, unit, and quantity  
✓ **Excel Export**: Generates formatted Excel reports with statistics  
✓ **Selector Caching**: Avoids repeated LLM calls by caching learned selectors  
✓ **Error Handling**: Robust handling of missing data and page errors  
✓ **Pagination Support**: Automatically follows pagination links  

## Architecture

```
intelligent-scraper/
├── config.py                 # Configuration and website setup
├── llm_agent.py             # LLM-based HTML analyzer
├── intelligent_spider.py    # Main Scrapy spider
├── data_pipeline.py         # Data processing and Excel export
├── run_scraper.py          # Main runner script
├── test_components.py      # Component tests (no API key needed)
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
└── output/                # Excel exports
```

## Installation

### 1. Clone/Setup Project
```bash
cd "d:\yourfolder\find scraping data"
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Full Scraper (Requires API Key)
```bash
python run_scraper.py
```

Then select option 1 to run the full scraper. You can specify which websites to scrape.

### Run Specific Websites
```python
from run_scraper import run_scraper
run_scraper(['hyperone', 'carrefour'])
```

## How It Works

### 1. Website Analysis Phase
- Spider fetches a sample page from the website
- LLM agent analyzes the HTML structure
- Detects CSS selectors for product fields (name, price, etc.)
- Caches these selectors for future use

### 2. Data Extraction Phase
- Spider iterates through product listings
- Uses learned selectors to extract data
- Falls back to LLM agent for difficult extractions
- Validates and normalizes all data

### 3. Pagination Phase
- Automatically detects and follows pagination links
- Limits to 3 pages per website (configurable)
- Continues extraction on each page

### 4. Export Phase
- All extracted data is processed through the pipeline
- Invalid items are filtered out
- Data is exported to formatted Excel file
- Summary sheet with statistics is created

## Data Structure

### Extracted Fields
```json
{
  "name": "Product Name",
  "price": 29.99,
  "discount": "15%",
  "unit": "1kg",
  "quantity": 150,
  "website": "hyperone",
  "scraped_at": "2024-01-15 14:30:00"
}
```

### Excel Output
- **Products Sheet**: All extracted products with all fields
- **Summary Sheet**: Statistics (total items, valid items, websites)
- **Formatting**: Header styling, borders, optimal column widths

## Configuration

### Adding New Websites
Edit `config.py` WEBSITES dictionary:
```python
WEBSITES = {
    'mynewsite': {
        'url': 'https://www.mynewsite.com',
        'search_url': 'https://www.mynewsite.com/search?q=',
        'category_url': 'https://www.mynewsite.com/products',
        'headers': {'User-Agent': '...'}
    }
}
```

## Output Files

### Excel File: `output/scraped_products.xlsx`
Contains:
- Products sheet with all extracted data
- Summary sheet with statistics
- Professional formatting with headers and borders

### Cache File: `cache/learned_selectors.json`
Stores learned selectors:
```json
{
  "hyperone": {
    "product_item": "div.product-item",
    "name_selector": "h2.product-name",
    ...
  }
}
```

## License

Created for educational and professional use.

---

**Ready to start?** Run: `python test_components.py`
