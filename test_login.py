import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Credentials
EMAIL = "neha@intervue.io"
PASSWORD = "Ps@neha@123"

# Setup
def test_login():
    # Start Chrome
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Open the website
        driver.get("https://www.intervue.io")

        # Click the Login button (top right corner)
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))
        )
        login_btn.click()

        # Wait for email input and enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(EMAIL)

        # Enter password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(PASSWORD)

        # Click the "Login" button
        submit_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Login']"))
        )
        submit_btn.click()

        # Wait for a dashboard element (or some logged-in confirmation)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Dashboard')]"))
        )
        print("✅ Login successful!")

    except TimeoutException:
        print("❌ Login failed. Taking screenshot.")
        driver.save_screenshot("login_failed.png")

    finally:
        # Give time to see the result and close
        time.sleep(2)
        driver.quit()
