from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def handle_easy_apply_popup(bot):
    try:
        # # Perform tasks on the pop-up
        # # Example: Fill in additional information, upload resume, etc.
        # # Wait for the pop-up to be visible
        # popup = bot.wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
        # )
        # # Example task: Fill in a text field in the pop-up
        # text_field = popup.find_element(By.CSS_SELECTOR, "input[name='example_field']")
        # text_field.send_keys("Example text")

        # # Example task: Click a button in the pop-up
        # submit_button = popup.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # submit_button.click()

        # Wait for and click the dismiss button
        dismiss_button = bot.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test-modal-close-btn]"))
        )
        dismiss_button.click()
        # Wait for and click the discard button
        discard_button = bot.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-test-dialog-secondary-btn]"))
        )
        discard_button.click()
        print("Handled Easy Apply pop-up successfully")
        time.sleep(3)
    except TimeoutException:
        print("Timeout while handling Easy Apply pop-up")
    except Exception as e:
        print(f"Error while handling Easy Apply pop-up: {str(e)}")
