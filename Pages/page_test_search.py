from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core import BrowserManager


class TestSearch:
    SEARCH = (By.XPATH, '//*[@role="combobox"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@role="search"]//button[@type="submit"]')

    def __init__(self, timeout, poll_frequency):
        self.browser = BrowserManager()
        self.timeout = timeout
        self.poll_frequency = poll_frequency
        self.wait = WebDriverWait(self.browser, self.timeout, self.poll_frequency)

    def wait_for_open(self):
        self.wait.until(
            EC.element_to_be_clickable(self.SEARCH)
        )

    def search_game(self, game):
        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH)
        )
        search.clear()
        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH)
        )
        search.send_keys(game)
        button_search = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        button_search.click()
