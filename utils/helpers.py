# helpers.py
from datetime import datetime

def print_test_message(message):
    print(f"Test: {message}")


def store_screenshot(driver, name):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename_stamp = f"logs/{name}_{timestamp}.png"
    #print(filename_stamp)
    driver.save_screenshot(filename_stamp)
    return filename_stamp
