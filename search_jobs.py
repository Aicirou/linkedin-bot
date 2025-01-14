from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def search_jobs(bot, job_title, location):
    try:
        # Navigate to LinkedIn Jobs
        bot.driver.get('https://www.linkedin.com/jobs/')

        # Find and fill job title
        job_title_field = bot.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search by title, skill, or company']"))
        )
        job_title_field.send_keys(job_title)

        # Find and fill location
        location_field = bot.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='City, state, or zip code']"))
        )
        location_field.clear()

        location_field.send_keys(location)

        # Wait for location suggestions to appear and select the first one
        first_location_suggestion = bot.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li[role='option']"))
        )
        first_location_suggestion.click()

        print(f"Searching for jobs with title: {job_title} in location: {location}")

        # Wait for search results to load
        time.sleep(3)

    except TimeoutException:
        print("Timeout while trying to search for jobs")
    except Exception as e:
        print(f"Error during job search: {str(e)}")
