# test_login.py
import time
import pytest
from config import config
# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime



# Store screenshot
def store_screenshot(driver, name):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"logs/{name}_{timestamp}.png"
    driver.save_screenshot(filename)

def test_login_valid():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(config.WEBSITE_URL)

    # Wait for and find the email input by aria-label
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Email"]'))
    )
    email_input.send_keys(config.VALID_USERNAME)
    #email_input.send_keys(VALID_USERNAME)

    # Find the password input by ID
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Password"]'))
    )
    password_input.send_keys(config.VALID_PASSWORD)
    #password_input.send_keys(VALID_PASSWORD)

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
    time.sleep(1.5)
    store_screenshot(driver,name="test_login_valid")

    #assert logout_button is not None
    assert profile is not None
    #driver.quit()
