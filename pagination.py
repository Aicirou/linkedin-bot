from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def go_to_next_page(bot):
    try:
        next_button = bot.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Next']"))
        )
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
        return True
    except TimeoutException:
        print("No more pages to navigate")
        return False
    except Exception as e:
        print(f"Error while navigating to the next page: {str(e)}")
        return False
