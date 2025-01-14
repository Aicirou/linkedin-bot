from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

def login(bot):
    try:
        # Navigate to LinkedIn
        bot.driver.get('https://www.linkedin.com/login')

        # Find and fill email
        email_field = bot.wait.until(

            EC.presence_of_element_located((By.ID, "username"))
        )
        email_field.send_keys(os.getenv('LINKEDIN_USERNAME'))

        # Find and fill password
        password_field = bot.wait.until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys(os.getenv('LINKEDIN_PASSWORD'))

        # Click login button
        login_button = bot.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()

        # Wait for login to complete
        time.sleep(10)

        return True

    except TimeoutException:
        print("Timeout while trying to log in")
        return False
    except Exception as e:
        print(f"Error during login: {str(e)}")
        return False
