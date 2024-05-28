import os
import pytest
from turbo2csv import TurboScraper

# Helper function to check if the output file exists and is not empty
def check_output_file(output_file):
    assert os.path.isfile(output_file)
    assert os.path.getsize(output_file) > 0

# Test scraping functionality
def test_scraping():
    output_file = 'test_turbo.csv'
    scraper = TurboScraper(geckodriver_path='geckodriver', headless=True)  # Assuming geckodriver is in the same directory
    scraper.scrape(output_file=output_file)
    check_output_file(output_file)

# Cleanup after testing
def teardown_module(module):
    os.remove('test_turbo.csv')

# You can add more test cases as needed
