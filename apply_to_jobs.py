from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time


def apply_to_jobs(bot):
    while True:
        try:
            ul_elements = bot.driver.find_elements(By.TAG_NAME, "ul")
            ul_element = None
            for ul in ul_elements:
                try:
                    li = ul.find_element(By.TAG_NAME, "li")
                    if li.get_attribute("data-occludable-job-id") is not None:
                        ul_element = ul
                        break
                except NoSuchElementException:
                    pass
            if ul_element is None:
                raise NoSuchElementException("Could not find the correct ul element")
        except NoSuchElementException:
            print("Could not find the correct ul element")
            exit()

        li_elements = ul_element.find_elements(By.TAG_NAME, "li")
        job_ids = []
        for li in li_elements:
            try:
                print("Getting job id")
                job_id = li.get_attribute("data-occludable-job-id")
                if job_id:
                    print(job_id)
                    job_ids.append(job_id)
            except Exception as e:
                print(f"An error occurred while trying to get the job id: {e}")

        click_count = 0
        for job_id in job_ids:
            try:
                li_with_job_id = WebDriverWait(bot.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f"li[data-occludable-job-id='{job_id}']"))
                )
                try:
                    job_list = li_with_job_id.find_element(By.CSS_SELECTOR, "ul.job-card-list__footer-wrapper li:last-child")
                    bot.driver.execute_script("arguments[0].click();", job_list)
                    print(f"Clicked 'Job List' for job ID: {job_id}")

                    # Wait for the Easy Apply button to be clickable and click it
                    easy_apply_button = bot.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, f"button[data-job-id='{job_id}']"))
                    )
                    easy_apply_button.click()

                    print(f"Confirmed 'Easy Apply' for job ID: {job_id}")

                    # Handle the Easy Apply pop-up
                    bot.handle_easy_apply_popup()

                    click_count += 1
                    if click_count % 4 == 0:
                        bot.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest' });", li_elements[-1])
                except NoSuchElementException:
                    print(f"Could not find 'Easy Apply' for job ID: {job_id}")
                time.sleep(2)
            except (TimeoutException, NoSuchElementException):
                print(f"Could not find or click 'Easy Apply' for job ID: {job_id}")
            except Exception as e:
                print(f"An error occurred while trying to click 'Easy Apply' for job ID {job_id}: {e}")

        if not bot.go_to_next_page():
            break
