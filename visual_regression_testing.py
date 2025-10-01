from selenium import webdriver
from applitools.selenium import Eyes, Target

# Initialize Applitools Eyes
eyes = Eyes()
eyes.api_key = 'your-applitools-api-key'  

# Start Visual Testing with Sauce Demo
try:
    
    driver = webdriver.Chrome()

    # Open the visual test session with Applitools
    eyes.open(
        driver=driver,
        app_name="Sauce Demo App",
        test_name="SauceDemo Visual Test Example",
        viewport_size={"width": 1200, "height": 800},
    )

    # Navigate to the Sauce Demo website
    driver.get("https://www.saucedemo.com/")

    # Perform visual checkpoints for different screens

    # Check the Login Page
    eyes.check("Login Page", Target.window())

    # Login into the application
    driver.find_element("id", "user-name").send_keys("standard_user")
    driver.find_element("id", "password").send_keys("secret_sauce")
    driver.find_element("id", "login-button").click()

    # Check the Products Page (Main Dashboard)
    eyes.check("Products Page", Target.window())

    # Open one of the product details
    driver.find_element("id", "item_4_title_link").click()

    # Check the Product Details Page
    eyes.check("Product Details Page", Target.window())

    # Close Applitools Eyes and complete the visual tests
    eyes.close_async()

finally:
    # Close the browser
    driver.quit()

    # In case of errors or aborts, ensure session is closed properly
    eyes.abort_if_not_closed()