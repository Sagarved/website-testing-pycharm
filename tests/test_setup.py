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
    # Store screenshot
    # timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    # filename = f"logs/test_check_{timestamp}.png"
    # To check conftest

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


def xtest_login_valid(driver):
    # Wait for and find the email input by aria-label
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Email"]'))
    )
    email_input.send_keys(config.VALID_USERNAME)

    # Find the password input by ID
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
    )
    password_input.send_keys(config.VALID_PASSWORD)

    # Optionally, submit the form
    # Assuming there's a submit button with aria-label="Login"
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Login"]'))
    )
    submit_button.click()
#
# def test_login_valid(driver):
#     driver.find_element(By.ARIA_LABLE, 'Email').send_keys(config.VALID_USERNAME)  # Replace 'username' with actual element selector
#     driver.find_element(By.ID, 'Password').send_keys(config.VALID_PASSWORD)  # Replace 'password' with actual element selector
#     driver.find_element(By.CLASS_NAME, 'submit').click()  # Replace 'submit' with actual element selector
#
#     # Add assertions to verify login success
#     assert 'Dashboard' in driver.title  # Example: checking the title after login

"""def test_login_invalid(driver):
    driver.find_element(By.NAME, 'username').send_keys('invalid_user')
    driver.find_element(By.NAME, 'password').send_keys('invalid_pass')
    driver.find_element(By.NAME, 'submit').click()

    # Add assertions to verify login failure
    assert 'Invalid credentials' in driver.page_source  # Example: checking for error message
"""