from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core import BrowserManager


class TestSearch:
    SEARCH = (By.XPATH, '//*[@role="combobox"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@role="search"]//button[@type="submit"]')
    SEARCH_RESULT = (By.XPATH, '//*[@id="searchtag_tmpl"][2]')
    SORT = (By.XPATH, '//*[@id="sort_by_trigger"]')
    HIGH_PRICE = (By.XPATH, '//*[@id="Price_DESC"]/..')
    COUNT_GAME = (By.XPATH, '//*[@id="search_resultsRows"]//a')
    FILTER_CHECK = (By.XPATH, '//*[@value="Price_DESC" and @id="sort_by" ]')
    BUTTON_LANGUAGE = (By.XPATH, '//*[@id="language_pulldown"]')
    LANGUAGE_EN = (By.XPATH, '//*[contains(@onclick, "english")]')

    def __init__(self, timeout):
        self.browser = BrowserManager()
        self.TIMEOUT = timeout
        self.wait = WebDriverWait(self.browser, self.TIMEOUT)

    def check_home_page(self):
        home = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH)
        )

    def search_game(self, game):
        search = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH)
        )
        search.clear()
        search.send_keys(game)
        button_search = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        button_search.click()

    def get_result_search(self):
        element = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_RESULT)
        )

        return element.get_attribute("data-tag_value")

    def sort_check(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.FILTER_CHECK)
        )

    def send_filter(self):
        sort = self.wait.until(
            EC.element_to_be_clickable(self.SORT)
        )
        sort.click()
        price = self.wait.until(
            EC.visibility_of_element_located(self.HIGH_PRICE)
        )
        price.click()

    def get_results_count(self):
        count_game = self.wait.until(
            EC.presence_of_all_elements_located(self.COUNT_GAME)
        )
        return len(count_game)
