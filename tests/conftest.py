import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from config import config
# wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check():
    # This is for chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://google.com")
    #driver.get(conf.WEBSITE_URL)
    driver.quit()


# Your test function
# def test_login_valid(driver):
#     # Your existing test code here
#     email_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Email"]'))
#     )
#     email_input.send_keys(config.VALID_USERNAME)
#
#     # Find the password input by ID
#     password_input = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
#     )
#     password_input.send_keys(config.VALID_PASSWORD)
#
#     # Optionally, submit the form
#     # Assuming there's a submit button with aria-label="Login"
#     submit_button = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Login"]'))
#     )
#     submit_button.click()
#     #
#     pass


