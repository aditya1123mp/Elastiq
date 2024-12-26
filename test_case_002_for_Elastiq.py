from selenium.webdriver.common.by import By
import time

def main(driver):
    try:
        # Wait for 3 seconds
        time.sleep(3)

        # Locate the search box using XPath
        search_box = driver.find_element(By.XPATH, "//div[@id='example_filter']/label/input[@type='search']")

        # Click on the search box
        search_box.click()

        # Enter 'New York' into the search box
        search_box.send_keys("New York")

        # Return the driver for further usage if needed
        return driver

    except Exception as e:
        print(f"An error occurred: {e}")
        if driver:
            driver.quit()
