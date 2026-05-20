# 🎯 WHICH FILE TO RUN - VISUAL GUIDE

## 🚀 MAIN ENTRY POINTS (What to Run)

```
┌─────────────────────────────────────────────────────────────────┐
│                    CHOOSE YOUR ACTION                           │
└─────────────────────────────────────────────────────────────────┘

1. "I want to see it work NOW!" (30 seconds)
   └─→ python demo_scraper.py
       └─→ output: demo_products.xlsx
           └─→ ✓ No API key needed
               ✓ Shows sample data
               ✓ Demo works in seconds

2. "Is my system set up correctly?" (30 seconds)
   └─→ python verify_system.py
       └─→ output: Detailed system status
           └─→ ✓ Checks all files
               ✓ Verifies dependencies
               ✓ Reports any issues

3. "Does everything work?" (30 seconds)
   └─→ python quick_test.py
       └─→ output: test_run.xlsx
           └─→ ✓ Tests all components
               ✓ Shows test results
               ✓ Confirms system ready

4. "I want to scrape real websites" (Requires API key)
   └─→ Step 1: Get API key
       └─→ Visit: https://platform.openai.com/api-keys
   └─→ Step 2: Create .env file
       └─→ cp .env.example .env
   └─→ Step 3: Add your API key
       └─→ Edit .env: OPENAI_API_KEY=sk-your-key
   └─→ Step 4: Run full scraper
       └─→ python run_scraper.py
           └─→ output: scraped_products.xlsx

5. "I want full testing" (5 minutes)
   └─→ python test_components.py
       └─→ output: Comprehensive test results
           └─→ ✓ Tests all 5 components
               ✓ Creates test Excel
               ✓ Shows all statistics
```

---

## 📁 ALL 25 FILES ORGANIZED

```
┌─────────────────────────────────────────────────────────────────┐
│               CORE MODULES (The Engine)                         │
│                    5 Python Files                               │
└─────────────────────────────────────────────────────────────────┘

config.py (2.5 KB)
  ├─ Websites: hyperone, carrefour
  ├─ API keys and settings
  ├─ Scraper configuration
  └─ LLM model selection

llm_agent.py (7.9 KB)
  ├─ OpenAI API integration
  ├─ HTML analysis
  ├─ Selector detection
  └─ Pattern caching

intelligent_spider.py (10.1 KB)
  ├─ Main Scrapy spider
  ├─ Product extraction
  ├─ Pagination handling
  └─ LLM-based adaptation

data_pipeline.py (7.9 KB)
  ├─ Data validation
  ├─ Data normalization
  ├─ Excel export
  └─ Statistics generation

optional_llm_agent.py (5.6 KB)
  ├─ Mock LLM (no API needed)
  ├─ Fallback mechanism
  └─ Testing support


┌─────────────────────────────────────────────────────────────────┐
│            RUNNER SCRIPTS (How to Execute)                      │
│                    5 Python Scripts                             │
└─────────────────────────────────────────────────────────────────┘

demo_scraper.py ⭐⭐⭐ (6.3 KB) [START HERE]
  ├─ No API key needed
  ├─ Sample data included
  └─ Creates demo_products.xlsx

run_scraper.py (7.0 KB) [Production]
  ├─ Menu-driven interface
  ├─ Requires API key
  └─ Scrapes real websites

quick_test.py (3.8 KB) [Verification]
  ├─ 30-second test
  ├─ Tests all components
  └─ Creates test_run.xlsx

verify_system.py (4.4 KB) [Setup Check]
  ├─ Checks files exist
  ├─ Verifies dependencies
  └─ Reports status

test_components.py (8.7 KB) [Full Testing]
  ├─ Comprehensive tests
  ├─ Tests 8 components
  └─ Detailed results


┌─────────────────────────────────────────────────────────────────┐
│           DOCUMENTATION (Reference Guides)                      │
│                    8 Markdown Files                             │
└─────────────────────────────────────────────────────────────────┘

00_START_HERE.md ⭐ (2 KB)
  └─ Read this first!

PROJECT_SUMMARY.md (10 KB)
  └─ Complete overview

README.md (7.2 KB)
  └─ Full technical docs

QUICKSTART.md (3.9 KB)
  └─ Quick reference

COMPLETION_REPORT.md
  └─ What was built

DELIVERY_REPORT.md
  └─ Project status

FINAL_SUMMARY.txt
  └─ Quick summary

INDEX.md
  └─ Navigation guide


┌─────────────────────────────────────────────────────────────────┐
│         CONFIGURATION (Settings & Templates)                    │
│                    3 Config Files                               │
└─────────────────────────────────────────────────────────────────┘

requirements.txt (170 B)
  └─ Python packages to install

.env.example (238 B)
  └─ API key template

.env (To Create)
  └─ Your actual API key


┌─────────────────────────────────────────────────────────────────┐
│            UTILITIES (Helper Scripts)                           │
│                    3 Helper Files                               │
└─────────────────────────────────────────────────────────────────┘

SUMMARY.py (9.8 KB)
  └─ Visual project summary

PROJECT_FILES.py (3.8 KB)
  └─ File verification

run_test.bat (374 B)
  └─ Windows batch runner
```

---

## 🔄 FILE DEPENDENCY FLOW

```
START HERE: Choose Your Path
│
├─→ Path 1: DEMO (No setup needed)
│   │
│   ├─ Run: demo_scraper.py
│   │   ├─ Imports: optional_llm_agent.py (mock)
│   │   ├─ Imports: data_pipeline.py
│   │   └─ Output: demo_products.xlsx
│   │
│   └─ Result: See working example in 30 seconds
│
├─→ Path 2: VERIFY (Quick check)
│   │
│   ├─ Run: verify_system.py
│   │   ├─ Checks: All files exist
│   │   ├─ Checks: Dependencies installed
│   │   └─ Creates: Output directories
│   │
│   └─ Result: System is ready to go
│
├─→ Path 3: TEST (Component testing)
│   │
│   ├─ Run: quick_test.py or test_components.py
│   │   ├─ Tests: config.py
│   │   ├─ Tests: llm_agent.py
│   │   ├─ Tests: data_pipeline.py
│   │   └─ Output: test_run.xlsx
│   │
│   └─ Result: All components working
│
└─→ Path 4: PRODUCTION (Real scraping)
    │
    ├─ Setup:
    │   ├─ Get API key
    │   ├─ Create .env file
    │   └─ Add OPENAI_API_KEY
    │
    ├─ Run: run_scraper.py
    │   ├─ Imports: config.py
    │   ├─ Starts: intelligent_spider.py
    │   │   ├─ Uses: llm_agent.py
    │   │   ├─ Uses: config.py
    │   │   └─ Calls: data_pipeline.py
    │   ├─ Imports: data_pipeline.py
    │   └─ Output: scraped_products.xlsx
    │
    └─ Result: Real website data in Excel


DETAILED PRODUCTION FLOW:
═════════════════════════

run_scraper.py
    ↓
1. Load config.py ← Settings, websites, API config
    ↓
2. Initialize intelligent_spider.py ← Main scraper
    ↓
3. For each website:
    ├─ Fetch page
    ├─ Send HTML to llm_agent.py ← AI analyzes
    │   ├─ Uses OpenAI API (from config.py)
    │   ├─ Detects CSS selectors
    │   └─ Caches result (for next time)
    ├─ Extract products using selectors
    ├─ Follow pagination links
    └─ Pass data to data_pipeline.py
    ↓
4. data_pipeline.py processes all products
    ├─ Validates each item
    ├─ Normalizes data
    ├─ Creates statistics
    └─ Exports to Excel
    ↓
5. Output: scraped_products.xlsx
```

---

## 📊 WHEN TO USE EACH FILE

```
SCENARIO 1: "I just installed everything"
├─ Step 1: python verify_system.py
│   └─ Ensures everything is in place
├─ Step 2: python quick_test.py
│   └─ Tests the system
└─ Step 3: Read 00_START_HERE.md
    └─ Understand the project

SCENARIO 2: "I want to see results immediately"
├─ Run: python demo_scraper.py
└─ Check: output/demo_products.xlsx

SCENARIO 3: "I want to scrape real websites"
├─ Step 1: Get API key
├─ Step 2: Create .env file with key
├─ Step 3: python run_scraper.py
└─ Step 4: Check output/scraped_products.xlsx

SCENARIO 4: "Something is broken"
├─ Run: python verify_system.py
│   └─ Check all files and setup
├─ Run: python quick_test.py
│   └─ Test each component
└─ Read: README.md
    └─ Find troubleshooting section

SCENARIO 5: "I want to understand the code"
├─ Read: PROJECT_SUMMARY.md
├─ Read: README.md
├─ Review: config.py (settings)
├─ Review: llm_agent.py (AI part)
├─ Review: intelligent_spider.py (scraper)
└─ Review: data_pipeline.py (export)

SCENARIO 6: "I want full testing"
├─ Run: python test_components.py
└─ Review: Detailed test results
```

---

## ✅ QUICK START CHECKLIST

### First Time Users:
```
[ ] 1. cd to project directory
[ ] 2. Run: python demo_scraper.py
[ ] 3. Open: output/demo_products.xlsx
[ ] 4. Read: 00_START_HERE.md
[ ] 5. Read: PROJECT_SUMMARY.md
[ ] 6. Decide next steps
```

### For Real Usage:
```
[ ] 1. Get API key from OpenAI
[ ] 2. Copy: cp .env.example .env
[ ] 3. Edit: .env (add your API key)
[ ] 4. Run: python run_scraper.py
[ ] 5. Choose: Select websites to scrape
[ ] 6. Wait: For scraping to complete
[ ] 7. Check: output/scraped_products.xlsx
```

### For Troubleshooting:
```
[ ] 1. Run: python verify_system.py
[ ] 2. Run: python quick_test.py
[ ] 3. Check: scraper.log
[ ] 4. Read: README.md (troubleshooting section)
[ ] 5. Review: Error messages carefully
```

---

## 🎯 FILE PURPOSES AT A GLANCE

| Need | Use This File | Command |
|------|---------------|---------|
| See demo | demo_scraper.py | `python demo_scraper.py` |
| Real scraping | run_scraper.py | `python run_scraper.py` |
| Quick test | quick_test.py | `python quick_test.py` |
| Verify setup | verify_system.py | `python verify_system.py` |
| Full testing | test_components.py | `python test_components.py` |
| Quick start | 00_START_HERE.md | Read it |
| Full guide | README.md | Read it |
| Configuration | config.py | Edit it |
| API setup | .env | Create & edit it |
| Dependencies | requirements.txt | `pip install -r requirements.txt` |

---

## 🏁 YOU'RE READY!

**Start with:**
```bash
python demo_scraper.py
```

**Check output:**
```
output/demo_products.xlsx
```

**Read documentation:**
```
00_START_HERE.md
```

Then you're ready to use the full system!

---

**Questions?**
- For quick answers: Read QUICKSTART.md
- For details: Read README.md
- For overview: Read PROJECT_SUMMARY.md
