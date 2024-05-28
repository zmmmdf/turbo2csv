from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from csv import writer
from time import sleep
import os

class TurboScraper:
    def __init__(self, geckodriver_path=None, headless=False):
        # Get the current directory of the script
        current_directory = os.path.dirname(os.path.realpath(__file__))
        # Specify the path to geckodriver
        self.geckodriver_path = geckodriver_path or os.path.join(current_directory, 'geckodriver')
        # Specify Firefox options
        self.firefox_options = webdriver.FirefoxOptions()
        if headless:
            self.firefox_options.add_argument('--headless')  # Run Firefox in headless mode

    def scrape(self, output_file='turbo.csv'):
        # Initialize Firefox driver with specified geckodriver path and options
        driver = webdriver.Firefox(executable_path=self.geckodriver_path, options=self.firefox_options)

        page = 1
        while True:
            with open(output_file, 'a') as turbo_csv:  # Append mode to avoid overwriting existing data
                csv_writer = writer(turbo_csv)

                # If it's the first page, write header row
                if page == 1:
                    csv_writer.writerow(['Name', 'Price', 'Year', 'Engine', 'Distance', 'City'])

                # Get the page URL
                page_url = f'https://turbo.az/autos?page={page}'
                driver.get(page_url)

                # Find all car elements on the page
                cars = driver.find_elements(By.CLASS_NAME, 'products-i__bottom')

                for car in cars:
                    try:
                        # Extract car details
                        name = car.find_element(By.CLASS_NAME, 'products-i__name').text
                        price = car.find_element(By.CLASS_NAME, 'product-price').text
                        year, engine, distance = car.find_element(By.CLASS_NAME, 'products-i__attributes').text.split(', ')
                        city = car.find_element(By.CLASS_NAME, 'products-i__datetime').text.split(',')[0]
                        print([name, price, year, engine, distance, city])
                        csv_writer.writerow([name, price, year, engine, distance, city])
                    except NoSuchElementException:
                        pass

            # Increment page number
            page += 1

            # Check if there's a next page
            try:
                driver.find_element(By.XPATH, "//a[text()='Next »']").click()
            except NoSuchElementException:
                break

            # Sleep to avoid overwhelming the server
            sleep(1)

        driver.quit()

# Example usage:
# scraper = TurboScraper()
# scraper.scrape(output_file='turbo.csv')
