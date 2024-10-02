# test_login.py

import pytest
from config import config
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import logging
from utils import helpers


#from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get(config.WEBSITE_URL)
# Setup logger
logger = logging.getLogger(__name__)

def test_check():
    # This is for chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://google.com")
    # Search input by ID
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'APjFqb'))
    )
    search_input.send_keys(config.VALID_USERNAME)
    logger.info("Entered search keyword")

    button = driver.find_element(By.CLASS_NAME, "gNO89b")
    driver.execute_script("arguments[0].click();", button)
    # Assert if search is not performed
    print(driver.title)
    logger.info(driver.title)

    WebDriverWait(driver, 10).until(
        EC.title_contains("Google")
    )


    filename_stamp = helpers.store_screenshot(driver,name="test_setup")
    logger.info("Before verification Test")
    # To check conftest
    logger.info(f'{filename_stamp}')
    logger.info(f'<img src={filename_stamp}" alt="{filename_stamp}" />')

    assert 'Google' in driver.title
    logger.info("After successful Test")

    # button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "gNO89b"))
    # )
    # button.click()
    # button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Google Search"]')
    # button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'gNO89b')))
    # button.click()

    # button = driver.find_element(By.CLASS_NAME, "gNO89b")
    # button.click()

    # Find and click the "Google Search" button using aria-label
    # search_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Google Search"]'))
    # )
    # search_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.NAME, 'btnK'))
    # )
    # search_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]'))
    # )

    #search_button.click()

    # Wait for search results
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, 'search'))
    # )
    #password_input.send_keys(config.VALID_PASSWORD)
    #search_input.send_keys(Keys.RETURN)
    #driver.get(conf.WEBSITE_URL)
    driver.quit()


