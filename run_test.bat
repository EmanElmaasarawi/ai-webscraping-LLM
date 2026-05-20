#!/usr/bin/env python
"""Batch test runner - standalone executable."""
import subprocess
import sys

# Try to run tests
try:
    result = subprocess.run([sys.executable, 'test_components.py'], cwd=r'd:\Eman Folder\Projects\webscraping- big data\find scraping data')
    sys.exit(result.returncode)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
