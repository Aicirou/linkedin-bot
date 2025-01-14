from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def filter_jobs(bot):
    try:
        # Click on "Date Posted" filter
        date_posted_filter = bot.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='searchFilter_timePostedRange']"))
        )
        date_posted_filter.click()

        # Select "Past 24 hours" option
        past_24_hours_option = bot.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='timePostedRange-r86400']"))
        )
        past_24_hours_option.click()

        # Add a small delay after clicking to let the results load
        time.sleep(10)

    except TimeoutException:
        print("Timeout while trying to filter jobs")
    except Exception as e:
        print(f"Error during job filtering: {str(e)}")
