from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main(driver=None):
    # Path to your WebDriver executable
    driver_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\chromedriver_26_12_2024\\chromedriver_26_12_2024\\chromedriver.exe"

    # Set ChromeOptions if needed
    chrome_options = Options()
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Initialize the Chrome driver using Service class
    driver_service = Service(driver_path)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

    # Maximize the window and navigate to the  site
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")

    return driver