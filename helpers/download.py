# helpers/download.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from config import THERAP_URL, USERNAME, PASSWORD, RAW_DATA_PATH

def download_report(report_name="ISP Data Detailed Report"):
    # Set up Selenium (Chrome example)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # run without opening a browser
    prefs = {"download.default_directory": os.path.abspath(RAW_DATA_PATH)}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get(THERAP_URL)

    # Log in
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login_button").click()

    time.sleep(5)  # wait for page to load

    # Navigate to report page and download (simplified example)
    # Replace with actual steps for your report
    driver.find_element(By.LINK_TEXT, report_name).click()
    driver.find_element(By.ID, "export_excel").click()

    time.sleep(5)  # wait for download to finish
    driver.quit()
