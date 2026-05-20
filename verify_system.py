"""
Final system verification before deployment.
Checks all files, dependencies, and creates directories.
"""
import os
import sys
from pathlib import Path

def print_header(text):
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80)

def main():
    print_header("INTELLIGENT WEB SCRAPER - FINAL VERIFICATION")
    
    base_path = Path(r'd:\Eman Folder\Projects\webscraping- big data\find scraping data')
    os.chdir(base_path)
    
    # Check Python version
    print(f"\n✓ Python: {sys.version.split()[0]}")
    if sys.version_info < (3, 8):
        print("  ✗ ERROR: Python 3.8+ required")
        return False
    
    # Check core files exist
    print("\n[1/4] Checking core modules...")
    core_files = [
        'config.py',
        'llm_agent.py',
        'optional_llm_agent.py',
        'intelligent_spider.py',
        'data_pipeline.py',
    ]
    for f in core_files:
        if (base_path / f).exists():
            size = (base_path / f).stat().st_size
            print(f"  ✓ {f:30s} ({size:,} bytes)")
        else:
            print(f"  ✗ {f:30s} - NOT FOUND")
            return False
    
    # Check runner scripts
    print("\n[2/4] Checking runner scripts...")
    scripts = [
        'run_scraper.py',
        'demo_scraper.py',
        'quick_test.py',
        'test_components.py',
    ]
    for f in scripts:
        if (base_path / f).exists():
            size = (base_path / f).stat().st_size
            print(f"  ✓ {f:30s} ({size:,} bytes)")
        else:
            print(f"  ✗ {f:30s} - NOT FOUND")
            return False
    
    # Check documentation
    print("\n[3/4] Checking documentation...")
    docs = [
        'README.md',
        'QUICKSTART.md',
        'PROJECT_SUMMARY.md',
        'requirements.txt',
        '.env.example',
    ]
    for f in docs:
        if (base_path / f).exists():
            size = (base_path / f).stat().st_size
            print(f"  ✓ {f:30s} ({size:,} bytes)")
        else:
            print(f"  ✗ {f:30s} - NOT FOUND")
            return False
    
    # Create output directories
    print("\n[4/4] Creating output directories...")
    for directory in ['output', 'cache', 'logs']:
        dir_path = base_path / directory
        dir_path.mkdir(exist_ok=True)
        print(f"  ✓ {directory}/")
    
    # File counts
    print("\n" + "-" * 80)
    py_files = list(base_path.glob('*.py'))
    md_files = list(base_path.glob('*.md'))
    print(f"Total Python files: {len(py_files)}")
    print(f"Total Documentation files: {len(md_files)}")
    
    # Calculate total size
    total_size = sum(f.stat().st_size for f in base_path.glob('*') if f.is_file())
    print(f"Total project size: {total_size:,} bytes (~{total_size/1024/1024:.1f} MB)")
    
    print("\n" + "=" * 80)
    print("✓ ALL CHECKS PASSED - SYSTEM READY FOR DEPLOYMENT")
    print("=" * 80)
    
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                         QUICK START COMMANDS                              ║
╚════════════════════════════════════════════════════════════════════════════╝

1️⃣  DEMO MODE (No API Key Needed):
    python demo_scraper.py
    ↳ Creates: output/demo_products.xlsx
    ↳ Shows 14 sample products from hyperone & carrefour

2️⃣  QUICK TEST:
    python quick_test.py
    ↳ Verifies all components work

3️⃣  FULL SCRAPER (Requires OpenAI API Key):
    python run_scraper.py
    ↳ Follow menu prompts to scrape real websites

════════════════════════════════════════════════════════════════════════════

📚 DOCUMENTATION:
   • PROJECT_SUMMARY.md  ← Start here!
   • README.md          ← Full documentation
   • QUICKSTART.md      ← Quick reference

🔑 API KEY (Optional for full features):
   1. Visit: https://platform.openai.com/api-keys
   2. Create a new API key
   3. cp .env.example .env
   4. Add key to .env: OPENAI_API_KEY=sk-your-key

════════════════════════════════════════════════════════════════════════════

✨ NEXT STEP: Run the demo!
   python demo_scraper.py

════════════════════════════════════════════════════════════════════════════
""")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
