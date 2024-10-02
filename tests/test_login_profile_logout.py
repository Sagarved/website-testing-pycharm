# test_login.py
import time
import pytest
import logging
from config import config
from utils import helpers
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver.get(config.WEBSITE_URL)

# Setup logger
logger = logging.getLogger(__name__)

#Load Chrome Driver
@pytest.fixture(scope="module")
def driver():
    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(config.WEBSITE_URL)
    yield driver
    driver.quit()


# @classmethod
# def setUpClass(self):
#     #driver_node = webdriver.Chrome(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     self.driver=driver_node
#     self.driver.maximize_window()
#     self.driver.get(WEBSITE_URL)

def test_login_valid_password(driver):
 # Wait for and find the email input by aria-label
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Email"]'))
    )
    email_input.send_keys(config.VALID_USERNAME)
    #email_input.send_keys(VALID_USERNAME)
    logger.info("Entered Email")
    # Find the password input by ID
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
    )
    password_input.send_keys(config.VALID_PASSWORD)
    #password_input.send_keys(VALID_PASSWORD)
    logger.info("Entered Password")


    # Optionally, submit the form
    # Assuming there's a submit button with aria-label="Login"
    submit_button = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Login"]'))
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/form/div[5]/button/span[3]"))
    )
    #     button = driver.find_element(By.CLASS_NAME, "gNO89b")
    #submit_button.click()
    driver.execute_script("arguments[0].click();", submit_button)
    # logout_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[2]/div/div/div[6]')))
    profile = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Profile"]')))
    time.sleep(1)
    helpers.store_screenshot(driver,name="test_login_valid_password")
    #assert logout_button is not None
    assert profile is not None
    logger.info("Test Passed")


# Profile detail update
# Select Profile after login
def test_profile_detail(driver):
    profile_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Profile"]')))
    driver.execute_script("arguments[0].click();", profile_button)
    company_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Company Name"]')))
    #company_name.clear()
    company_name.send_keys(config.COMPANY_NAME)
    # Save and verify message
    profile_detail_save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div/div[2]/div[6]/div/button[2]/span[3]'))
    )
    driver.execute_script("arguments[0].click();", profile_detail_save_button)
    logger.info("Updated Profile Detail")
    #Check message
    save_message = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/h3'))
    )
    time.sleep(1)
    helpers.store_screenshot(driver, name="test_profile_detail")
    assert "User details successfully updated" in save_message.text
    logger.info("Test Passed")
# Change password
def xtest_password(driver):
    current_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div[1]/div/div[3]/label[2]/text()'))
    )
    current_password.send_keys(config.VALID_PASSWORD)
    # Enter value for new password and verify password
    new_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div/div[1]/div/div[3]/label[2]/text()')))
    verify_password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[1]/div[3]/div/div[1]/div/div[3]/label[2]/text()')))
    new_password.send_keys(config.NEW_PASSWORD)
    verify_password.send_keys(config.NEW_PASSWORD)

    # Save Password
    save_password_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[2]/button[2]/span[3]')))
    driver.execute_script("arguments[0].click();", save_password_button)

    #Check successful message
    password_save_message = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/h3'))
    )
    time.sleep(1)
    helpers.store_screenshot(driver, name="test_password_detail")
    assert "Password successfully updated" in password_save_message.text

    # #re-login and cleanup
    # # logout
    # test_logout()
    # # login button
    # login_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[2]/div/div/a[2]')))
    # driver.execute_script("arguments[0].click();", login_button)
    # test_login_valid_password()

def test_logout(driver):
    logout_button = WebDriverWait(driver, 10).until(
        #EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Login"]'))
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[2]/div/div/div[6]'))
    )
    #submit_button.click()
    driver.execute_script("arguments[0].click();", logout_button)
    logger.info("User Logged Out")
    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[2]/div/div/a[2]')))
    time.sleep(1)
    helpers.store_screenshot(driver, name="test_logout")
    assert login is not None
    logger.info("Test Passed")

def test_login_invalid_password(driver):
    # Select Login
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div[2]/div/div/a[2]')))
    driver.execute_script("arguments[0].click();", login_button)
    # Wait for and find the email input by aria-label
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Email"]'))
    )
    email_input.send_keys(config.INVALID_USERNAME)
    # email_input.send_keys(VALID_USERNAME)
    logger.info("Email Entered")
    # Find the password input by ID
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
    )
    password_input.send_keys(config.INVALID_PASSWORD)
    # password_input.send_keys(VALID_PASSWORD)
    logger.info("Wrong Password Entered")

    # Optionally, submit the form
    # Assuming there's a submit button with aria-label="Login"
    submit_button = WebDriverWait(driver, 10).until(
        # EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Login"]'))
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/div/form/div[5]/button/span[3]"))
    )
    #     button = driver.find_element(By.CLASS_NAME, "gNO89b")
    # submit_button.click()
    driver.execute_script("arguments[0].click();", submit_button)

    error_msg = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/h3')))
    time.sleep(1)
    helpers.store_screenshot(driver, name="test_login_invalid_password")
    # assert logout_button is not None
    assert 'Incorrect' in  error_msg.text
    logger.info("Test Passed")
# To validate forgot password field
def xtest_forgot_password(driver):
    #manual due to passcode sent to email
    pass


