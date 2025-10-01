from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


driver = webdriver.Chrome()
driver.maximize_window()

# Self-Healing Locator Function
def find_element_self_healing(driver, primary_locator_type, primary_locator_value, fallback_locator_type, fallback_locator_value):
    """
    Attempts to locate an element using a primary locator and falls back to an alternative locator if the primary fails.
    """
    try:
        # Primary locator attempt
        logging.info("Trying primary locator...")
        element = driver.find_element(primary_locator_type, primary_locator_value)
        logging.info("Element found using primary locator.")
    except NoSuchElementException:
        # Fallback locator attempt
        logging.warning("Primary locator failed. Trying fallback...")
        element = driver.find_element(fallback_locator_type, fallback_locator_value)
        logging.info("Element found using fallback locator.")
    return element


try:
    # Navigate to SauceDemo
    driver.get("https://www.saucedemo.com/")

    # 1. Find the username field
    username_field = find_element_self_healing(
        driver,
        #By.ID, "user-name",                         # Primary locator: ID
        By.ID, "user-nam",               # Primary locator: ID
        By.XPATH, "//input[@data-test='username']"  # Fallback locator: XPath
    )
    username_field.send_keys("standard_user")  # Enter the dummy username

    # 2. Find the password field
    password_field = find_element_self_healing(
        driver,
        # By.ID, "password",                # Primary locator: ID
        By.ID, "passwor",                # Primary locator: ID
        By.XPATH, "//input[@data-test='password']"  # Fallback locator: XPath
    )
    password_field.send_keys("secret_sauce")  # Enter the dummy password

    # 3. Find and click the login button
    login_button = find_element_self_healing(
        driver,
        By.ID, "login-button",            # Primary locator: ID
        By.XPATH, "//input[@data-test='login-button']"  # Fallback locator: XPath
    )
    login_button.click()

    # Log confirmation message
    logging.info("Login button clicked. Attempting login...")

    # 4. Validate login success by checking URL or a specific element on the next page
    if "inventory.html" in driver.current_url:
        logging.info("Login successful! Redirected to inventory page.")
    else:
        logging.error("Login failed. Please check credentials or page behavior.")

finally:
    driver.quit()