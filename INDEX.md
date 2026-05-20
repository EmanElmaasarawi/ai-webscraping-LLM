# Intelligent Web Scraper with LLM Agent
## Complete Project Index

### 📋 WHAT IS THIS?
A professional web scraper that uses AI/LLM to automatically detect and adapt to different website designs. Extracts product information and exports to Excel.

**Extracted Data**: Name, Price, Discount, Unit, Quantity

---

## 🚀 QUICK START (Choose One)

### Option A: Try Demo (2 min, no API key)
```bash
python demo_scraper.py
```
Creates `output/demo_products.xlsx` with sample data

### Option B: Verify System (2 min)
```bash
python verify_system.py
```
Checks all files and dependencies

### Option C: Run Tests (5 min)
```bash
python quick_test.py
```
Tests all components

---

## 📂 PROJECT FILES

### Core Scraping Modules
- **config.py** - Configuration, websites, API keys
- **llm_agent.py** - Real LLM agent (requires API key)
- **optional_llm_agent.py** - LLM with mock fallback
- **intelligent_spider.py** - Main Scrapy spider
- **data_pipeline.py** - Data processing & Excel export

### Runner Scripts
- **run_scraper.py** - Main menu-driven runner
- **demo_scraper.py** - Demo with sample data ⭐
- **quick_test.py** - Quick verification
- **test_components.py** - Full component tests
- **verify_system.py** - System verification

### Documentation
- **README.md** - Complete documentation
- **QUICKSTART.md** - Quick start guide
- **PROJECT_SUMMARY.md** - Comprehensive summary
- **PROJECT_FILES.py** - File verification tool
- **INDEX.md** - This file

### Configuration
- **requirements.txt** - Python dependencies
- **.env.example** - Environment template
- **.env** - Your API key (create from .env.example)

### Output Directories
- **output/** - Excel files created here
- **cache/** - Learned selectors stored here
- **logs/** - Log files

---

## 🎯 KEY FEATURES

✓ **LLM-Based Detection** - Analyzes HTML to understand website structure  
✓ **Multi-Site Support** - Works with hyperone, carrefour, etc.  
✓ **Intelligent Adaptation** - Learns CSS selectors for each website  
✓ **Data Extraction** - Name, price, discount, unit, quantity  
✓ **Excel Export** - Professional formatted output with statistics  
✓ **Selector Caching** - Avoids repeated LLM calls  
✓ **Pagination** - Automatically follows page links  
✓ **Error Handling** - Robust and fault-tolerant  
✓ **Mock Mode** - Works without API key for testing  

---

## 📊 WHAT YOU GET

### Excel Output
```
Sheet 1: Products
├── Name (Product name)
├── Price (Numeric value)
├── Discount (% or amount)
├── Unit (kg, L, piece, etc.)
├── Quantity (Available stock)
├── Website (Source)
└── Scraped At (Timestamp)

Sheet 2: Summary
├── Total Items Scraped
├── Valid Items
├── Invalid Items
├── Websites Scraped
└── Export Date
```

---

## 🔑 API KEY SETUP (Optional)

### Why API Key?
- **Without**: Demo mode works, uses mock data
- **With**: Full scraping with real LLM intelligence

### Get API Key
1. Visit: https://platform.openai.com/api-keys
2. Create new secret key
3. Copy key (starts with `sk-`)

### Configure
```bash
cp .env.example .env
# Edit .env and add: OPENAI_API_KEY=sk-your-key-here
```

---

## ✅ VERIFICATION CHECKLIST

- [ ] Python 3.8+ installed
- [ ] Run: `python verify_system.py`
- [ ] Run: `python demo_scraper.py`
- [ ] Check: `output/demo_products.xlsx` created
- [ ] Read: `PROJECT_SUMMARY.md`
- [ ] (Optional) Get API key for full features
- [ ] (Optional) Run: `python run_scraper.py`

---

## 🛠️ SYSTEM REQUIREMENTS

- Python 3.8+
- Internet connection
- ~50MB disk space
- (Optional) OpenAI API key for real scraping

---

## 📈 WHAT'S INSIDE EACH FILE

### config.py (2549 bytes)
- Website configurations
- API key settings
- Scraper settings
- LLM prompts
- Export configuration

### llm_agent.py (7865 bytes)
- LLMAgent class for real API calls
- SelectorCache for caching learned patterns
- Error handling and validation

### intelligent_spider.py (10116 bytes)
- Main Scrapy spider
- Product extraction logic
- Pagination handling
- LLM-based adaptation

### data_pipeline.py (7940 bytes)
- Data validation
- Data normalization
- Excel export with formatting
- Statistics tracking

### demo_scraper.py (6329 bytes)
- Demo data for hyperone
- Demo data for carrefour
- Excel export demonstration
- No API key required

### run_scraper.py (6982 bytes)
- Menu-driven runner
- Environment setup
- Dependency checking
- Component testing

---

## 🚀 DEPLOYMENT CHECKLIST

- [x] All core modules implemented
- [x] Excel export functionality
- [x] Data pipeline complete
- [x] LLM integration ready
- [x] Mock fallback included
- [x] Demo data provided
- [x] Complete documentation
- [x] Test scripts included
- [x] Configuration ready
- [x] Ready for production

---

## 📞 TROUBLESHOOTING

### Issue: "Missing packages"
**Solution**: `pip install -r requirements.txt`

### Issue: "API key not found"
**Solution**: Create .env file with your key

### Issue: "No data being extracted"
**Solution**: Clear cache: `delete cache/learned_selectors.json`

### Issue: "LLM errors"
**Solution**: Check API key validity and account credits

See `README.md` and `QUICKSTART.md` for more help.

---

## 📚 DOCUMENTATION MAP

| Document | Purpose |
|----------|---------|
| **PROJECT_SUMMARY.md** | Complete overview (start here!) |
| **README.md** | Full technical documentation |
| **QUICKSTART.md** | Quick reference guide |
| **INDEX.md** | This file |
| **PROJECT_FILES.py** | File verification tool |

---

## 🎯 NEXT ACTIONS

### Immediate (Right Now)
1. Read this file
2. Check `PROJECT_SUMMARY.md`

### Short Term (Next 5 minutes)
1. Run: `python demo_scraper.py`
2. Check: `output/demo_products.xlsx`
3. Verify system works

### Medium Term (Next 30 minutes)
1. Read: `README.md`
2. Get API key (optional): https://platform.openai.com/api-keys
3. Create: `.env` file
4. Configure: Add your API key

### Long Term (Ready to use)
1. Run: `python run_scraper.py`
2. Customize: Add more websites in `config.py`
3. Deploy: Use in production

---

## ✨ SUCCESS INDICATORS

- [x] All Python files created
- [x] All documentation complete
- [x] Configuration templates ready
- [x] Demo data available
- [x] Test scripts included
- [x] Output directories created
- [x] System verified working
- [x] Ready for testing

---

## 🎉 YOU'RE ALL SET!

### Run This Now:
```bash
python demo_scraper.py
```

### Then Check:
`output/demo_products.xlsx`

### For Help:
Read `PROJECT_SUMMARY.md`

---

**Status**: ✓ Complete and Ready for Testing  
**Created**: January 2024  
**Version**: 1.0  
**License**: For educational and professional use  

---

## Navigation
- [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Comprehensive overview
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick reference
