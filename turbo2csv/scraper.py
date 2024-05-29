from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer
from time import sleep
import os

class TurboScraper:
    def __init__(self, geckodriver_path=None, headless=False):
        current_directory = os.path.dirname(os.path.realpath(__file__))
        self.geckodriver_path = geckodriver_path or os.path.join(current_directory, 'geckodriver')
        self.firefox_options = webdriver.FirefoxOptions()
        if headless:
            self.firefox_options.add_argument('--headless')

    def scrape(self, output_file='turbo.csv', start=1):
        driver = webdriver.Firefox(executable_path=self.geckodriver_path, options=self.firefox_options)
        page_url = 'https://turbo.az/autos'
        driver.get(page_url)
        
        # Finding the last page number
        last_page_element = driver.find_element(By.CSS_SELECTOR, '.last a')
        last_page_url = last_page_element.get_attribute('href')
        last_page_number = int(last_page_url.split('=')[-1])
        
        # Displaying the range of pages to be scraped
        print(f"Starting the scraping process from page {start} to page {last_page_number}")
        
        unique_entries = set()

        for page in range(start, last_page_number + 1):
            page_url = f'https://turbo.az/autos?page={page}'
            driver.get(page_url)
            sleep(2)  # Adding a slight delay to ensure the page loads completely
            
            # Logging the current page being processed
            print(f"Scraping page {page}/{last_page_number}...")

            cars = driver.find_elements(By.CLASS_NAME, 'products-i__bottom')
            for car in cars:
                try:
                    name = car.find_element(By.CLASS_NAME, 'products-i__name').text
                    price = car.find_element(By.CLASS_NAME, 'product-price').text
                    year, engine, distance = car.find_element(By.CLASS_NAME, 'products-i__attributes').text.split(', ')
                    city = car.find_element(By.CLASS_NAME, 'products-i__datetime').text.split(',')[0]
                    entry = (name, price, year, engine, distance, city)
                    
                    # Logging each entry found
                    print(f"Found entry: {entry}")
                    
                    if entry not in unique_entries:
                        unique_entries.add(entry)
                except NoSuchElementException:
                    # Logging an error if an element is not found
                    print(f"Error processing car entry on page {page}")
                    pass
            
            # Logging completion of page scraping
            print(f"Completed scraping page {page}")

        # Writing to CSV file
        with open(output_file, 'w', newline='') as turbo_csv:
            csv_writer = writer(turbo_csv)
            csv_writer.writerow(['Name', 'Price', 'Year', 'Engine', 'Distance', 'City'])
            for entry in unique_entries:
                csv_writer.writerow(entry)

        # Logging the completion of the scraping process
        print(f"Scraping completed. Total unique entries found: {len(unique_entries)}")
        print(f"Data saved to {output_file}")
        
        driver.quit()
