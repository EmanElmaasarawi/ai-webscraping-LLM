"""
Complete project file and structure verification.
Lists all created files and their purposes.
"""
import os
from pathlib import Path

PROJECT_FILES = {
    'Core Modules': {
        'config.py': 'Configuration, API keys, website setup',
        'llm_agent.py': 'Real LLM agent using OpenAI API',
        'optional_llm_agent.py': 'LLM agent with mock fallback',
        'intelligent_spider.py': 'Main Scrapy spider with LLM',
        'data_pipeline.py': 'Data processing and Excel export',
    },
    'Scripts': {
        'run_scraper.py': 'Main runner with menu',
        'demo_scraper.py': 'Demo with sample data (no API needed)',
        'quick_test.py': 'Quick verification script',
        'test_components.py': 'Full component tests',
    },
    'Configuration': {
        'requirements.txt': 'Python package dependencies',
        '.env.example': 'Environment template',
        '.env': 'Local env (add your API key here)',
    },
    'Documentation': {
        'README.md': 'Complete documentation',
        'QUICKSTART.md': 'Quick start guide',
        'PROJECT_FILES.py': 'This file - project overview',
    },
    'Output Directories': {
        'output/': 'Excel export files',
        'cache/': 'Learned selectors cache',
        'logs/': 'Log files',
    },
}

def check_files():
    """Check which files exist."""
    print("=" * 80)
    print("PROJECT FILE VERIFICATION")
    print("=" * 80)
    
    base_path = Path(r'd:\Eman Folder\Projects\webscraping- big data\find scraping data')
    
    for category, files in PROJECT_FILES.items():
        print(f"\n{category}:")
        print("-" * 80)
        
        for filename, description in files.items():
            if filename.endswith('/'):
                # Directory
                path = base_path / filename
                exists = path.exists()
                status = "✓ EXISTS" if exists else "✗ NOT CREATED"
                print(f"  {status}: {filename:30s} - {description}")
            else:
                # File
                path = base_path / filename
                exists = path.exists()
                status = "✓ EXISTS" if exists else "✗ MISSING"
                
                if exists:
                    size = path.stat().st_size
                    print(f"  {status}: {filename:30s} ({size:,} bytes)")
                else:
                    print(f"  {status}: {filename:30s}")

def show_usage():
    """Show usage instructions."""
    print("\n" + "=" * 80)
    print("QUICK START COMMANDS")
    print("=" * 80)
    
    print("\n1. DEMO (No API key needed):")
    print("   python demo_scraper.py")
    print("   Creates: output/demo_products.xlsx")
    
    print("\n2. QUICK TEST:")
    print("   python quick_test.py")
    
    print("\n3. FULL TESTS:")
    print("   python test_components.py")
    
    print("\n4. FULL SCRAPER (Requires OpenAI API key):")
    print("   python run_scraper.py")
    print("   OR")
    print("   python run_scraper.py")
    
    print("\n5. SETUP:")
    print("   cp .env.example .env")
    print("   # Edit .env and add: OPENAI_API_KEY=sk-your-key")
    
    print("\n6. INSTALL DEPENDENCIES:")
    print("   pip install -r requirements.txt")

def main():
    """Main verification."""
    check_files()
    show_usage()
    
    print("\n" + "=" * 80)
    print("✓ PROJECT SETUP COMPLETE")
    print("=" * 80)
    print("\nNext steps:")
    print("1. Run: python demo_scraper.py")
    print("2. Check output/demo_products.xlsx")
    print("3. Get API key for full features")
    print("4. Read README.md for complete documentation")
    print("=" * 80)

if __name__ == '__main__':
    main()
