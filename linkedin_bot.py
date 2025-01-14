from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from dotenv import load_dotenv
from login import login
from search_jobs import search_jobs
from filter_jobs import filter_jobs
from apply_to_jobs import apply_to_jobs
from handle_easy_apply_popup import handle_easy_apply_popup
from pagination import go_to_next_page

class LinkedInBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        load_dotenv()

    def login(self):
        return login(self)

    def search_jobs(self, job_title, location):
        search_jobs(self, job_title, location)

    def filter_jobs(self):
        filter_jobs(self)

    def handle_easy_apply_popup(self):
        handle_easy_apply_popup(self)

    def apply_to_jobs(self):
        apply_to_jobs(self)

    def go_to_next_page(self):
        return go_to_next_page(self)

    def close(self):
        self.driver.quit()
