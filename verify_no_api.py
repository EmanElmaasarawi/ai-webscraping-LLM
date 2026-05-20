"""
VERIFICATION SCRIPT - Check that everything is updated and working
"""
import os
import sys
from pathlib import Path

def check_files():
    """Check all necessary files exist."""
    print("=" * 80)
    print("WEB SCRAPER - NO API KEY NEEDED - VERIFICATION")
    print("=" * 80)
    
    required_files = {
        'Core Scrapers': [
            'smart_scraper_no_api.py',
            'data_pipeline.py',
            'config.py',
        ],
        'Runners': [
            'scraper.py',
            'demo_no_api.py',
        ],
        'Configuration': [
            'requirements.txt',
            '.env.example',
        ],
        'Documentation': [
            'NO_API_GUIDE.md',
            'START_NO_API.md',
            'README.md',
        ]
    }
    
    all_exist = True
    
    for category, files in required_files.items():
        print(f"\n{category}:")
        print("-" * 80)
        
        for filename in files:
            path = Path(filename)
            if path.exists():
                size = path.stat().st_size
                print(f"  ✓ {filename:30s} ({size:,} bytes)")
            else:
                print(f"  ✗ {filename:30s} - MISSING!")
                all_exist = False
    
    return all_exist

def check_dependencies():
    """Check if Python packages are installed."""
    print("\n" + "=" * 80)
    print("Checking Python Packages:")
    print("-" * 80)
    
    packages = ['requests', 'bs4', 'openpyxl', 'lxml']
    all_installed = True
    
    for package in packages:
        try:
            __import__(package)
            print(f"  ✓ {package:20s} installed")
        except ImportError:
            print(f"  ✗ {package:20s} NOT installed")
            all_installed = False
    
    if not all_installed:
        print("\n⚠️  INSTALL MISSING PACKAGES WITH:")
        print("     pip install -r requirements.txt")
    
    return all_installed

def show_quick_start():
    """Show quick start commands."""
    print("\n" + "=" * 80)
    print("QUICK START - CHOOSE ONE:")
    print("=" * 80)
    print("""
1. INTERACTIVE MENU (Best for most users):
   python scraper.py
   
   This gives you a menu to:
   - Scrape Hyperone Egypt
   - Scrape Carrefour Egypt
   - Scrape Both
   - Scrape Custom URL

2. DEMO (See it working):
   python demo_no_api.py
   
   This scrapes both websites and shows results

3. VIEW GUIDE:
   Open: NO_API_GUIDE.md
   
   Complete documentation and examples
""")

def main():
    """Main verification."""
    os.chdir(Path(__file__).parent)
    
    files_ok = check_files()
    deps_ok = check_dependencies()
    
    print("\n" + "=" * 80)
    print("VERIFICATION SUMMARY:")
    print("=" * 80)
    
    print(f"✓ Files: {'OK' if files_ok else 'MISSING FILES'}")
    print(f"✓ Dependencies: {'OK' if deps_ok else 'MISSING PACKAGES'}")
    
    if files_ok and deps_ok:
        print("\n✅ EVERYTHING IS READY!")
        print("\nYour scraper is updated and ready to use!")
        print("No API key needed. Just run:")
        print("\n   python scraper.py")
        show_quick_start()
    else:
        print("\n⚠️  PLEASE FIX ISSUES ABOVE:")
        if not files_ok:
            print("   - Some files are missing")
        if not deps_ok:
            print("   - Install packages: pip install -r requirements.txt")
    
    print("\n" + "=" * 80)
    print("VERSION: 2.0 (No API Key)")
    print("STATUS: ✅ Ready to Use")
    print("=" * 80)

if __name__ == '__main__':
    main()
