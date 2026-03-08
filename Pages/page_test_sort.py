from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core import BrowserManager


class TestSort:
    SEARCH_RESULT = (By.XPATH, '//*[@id="searchtag_tmpl"][2]')
    SORT = (By.ID, "sort_by_trigger")
    HIGH_PRICE = (By.XPATH, '//*[@id="Price_DESC"]/..')
    COUNT_GAME = (By.XPATH, '//*[@id="search_resultsRows"]//a')
    PRICE_GAME = (By.XPATH, '//*[contains(@class, "discount_final_price")]')
    SEARCH_RESULT_GAME = (By.ID, 'search_result_container')
    LOADING_SORT = (By.XPATH, '//*[contains(@style, "opacity")and @id="search_result_container"]')

    def __init__(self, timeout, poll_frequency):
        self.browser = BrowserManager()
        self.timeout = timeout
        self.poll_frequency = poll_frequency
        self.wait = WebDriverWait(self.browser, self.timeout, self.poll_frequency)

    def get_result_search(self):
        element = self.wait.until(
            EC.presence_of_element_located(self.SEARCH_RESULT)
        )

        return element.get_attribute("data-tag_value")

    def wait_for_sort(self):
        self.wait.until(
            EC.presence_of_element_located(self.LOADING_SORT)
        )
        self.wait.until_not(
            EC.presence_of_element_located(self.LOADING_SORT)
        )

    def send_filter(self):
        sort = self.wait.until(
            EC.element_to_be_clickable(self.SORT)
        )
        sort.click()
        price = self.wait.until(
            EC.element_to_be_clickable(self.HIGH_PRICE)
        )
        price.click()

    def get_results_count(self):
        count_game = self.wait.until(
            EC.presence_of_all_elements_located(self.COUNT_GAME)
        )

        return len(count_game)

    def get_list_price_game(self, n):
        price_game = self.wait.until(
            EC.presence_of_all_elements_located(self.PRICE_GAME)
        )[:n]
        list_game = []
        for i in price_game:
            price = i.get_attribute("textContent").replace(" руб", "").replace(",", ".")
            if price == "Бесплатно" or price == "Free":
                list_game.append(0)
            else:
                list_game.append(float(price))
        return list_game

    def check_loading_search_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_RESULT_GAME)
        )
