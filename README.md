Turbo.az Scraper
================

This is a Python web scraper built to extract car information from Turbo.az, one of the most popular car purchase websites in Azerbaijan. 

Features
--------

-   Extracts car details including make, model, year, price, and location.
-   Data is saved in CSV format.
-   Selenium and Beautiful Soup libraries are used for web scraping.
-   Code may need to be updated due to possible changes in website HTML tags.

Installation
------------

1.  Clone this repository.
2.  Install the required dependencies by running `pip install -r requirements.txt` in your terminal.

Installation
----------

You can install turbo2csv via pip:

```bash
pip install turbo2csv
```

Usage
----------
```py
from turbo2csv import   

scraper = TurboScraper()
scraper.scrape(output_file='turbo.csv')

```


### Testing

turbo2csv includes comprehensive test coverage to ensure reliability and accuracy. To run the tests, you can use pytest:

```bash
pip install pytest
pytest
```

Disclaimer
----------

This application is intended for educational purposes only and should not be used for commercial purposes. The author is not responsible for any legal issues that may arise from the misuse of this tool.

License
-------

This project is licensed under the MIT License - see the LICENSE file for details.
