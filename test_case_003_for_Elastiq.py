from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def main(driver=None):
    # If no driver is passed, set up a new ChromeDriver
    if driver is None:
        chrome_options = Options()
        driver_service = Service("C:\\Users\\DELL\\OneDrive\\Desktop\\chromedriver_26_12_2024\\chromedriver_26_12_2024\\chromedriver.exe")  # Replace with the path to your chromedriver
        driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    try:
        # Navigate to the URL (replace with the actual URL of the page)
        #driver.get("URL_of_the_page")  # Replace with the target URL

        # Define the XPath
        xpath = "//table[@id='example']//tr[@role='row']//td[3]"

        # Find all elements matching the XPath
        rows = driver.find_elements(By.XPATH, xpath)

        # Get the count of rows
        row_count = len(rows)
        # Wait for 3 seconds
        time.sleep(3)

        # Check if the row count is 5
        if row_count == 5:
            print("Yes, 5 rows are present")
        else:
            print(f"Row count is: {row_count}")
        # Wait for 3 seconds
        time.sleep(3)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the driver only if it was created within this function
        if driver is not None:
            driver.quit()

    return driver
