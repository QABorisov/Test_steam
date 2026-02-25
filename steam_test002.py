from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class BrowserManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance=webdriver.Chrome()
        return cls._instance

    @classmethod
    def close(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance=None

@pytest.fixture(scope="session")
def browser():
    browser = BrowserManager()
    yield browser
    BrowserManager.close()


class TestSearch:
    def __init__(self, browser):
        self.browser = browser
        self.LINK = "https://store.steampowered.com/"
        self.TIMEOUT = 5
        self.SEARCH = (By.XPATH, '//*[@role="combobox"]')
        self.SEARCH_BUTTON = (By.XPATH, '//*[@role="search"]//button[@type="submit"]')
        self.SEARCH_RESULT = (By.XPATH, '//*[contains(@class, "tag_dynamic")]')  # тут надо разбить классы контаинс
        self.SORT = (By.XPATH, '//*[@id="sort_by_trigger"]')
        self.HIGH_PRICE = (By.XPATH, '//*[@id="Price_DESC"]/..')
        self.COUNT_GAME = (By.XPATH, '//*[@id="search_resultsRows"]//a')
        self.FILTER_CHECK = (By.XPATH, '//*[@value="Price_DESC" and @id="sort_by" ]')

    def search_game(self, game):
        search = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCH)
        )
        search.clear()
        search.send_keys(game)
        button_search = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        )
        button_search.click()

    def get_result_search(self):
        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCH_RESULT)
        )

        return element.get_attribute("data-tag_value")

    def sort_check(self):
        element = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.presence_of_element_located(self.FILTER_CHECK)
        )

    def send_filter(self):
        sort = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.element_to_be_clickable(self.SORT)
        )
        sort.click()
        price = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.HIGH_PRICE)
        )
        price.click()

    def get_results_count(self):
        count_game = WebDriverWait(self.browser, self.TIMEOUT).until(
            EC.presence_of_all_elements_located(self.COUNT_GAME)
        )
        return len(count_game)


@pytest.mark.parametrize("game_name, min_count",
                         [
                             ("The Witcher", 10),
                             ("Fallout", 20)
                         ])
def test_steam(browser, game_name, min_count):
    search_with_sorting = TestSearch(browser)
    browser.get(search_with_sorting.LINK)
    search_with_sorting.search_game(game_name)
    assert search_with_sorting.get_result_search() == game_name, f"Не перешли на страницу с результатами поиска"
    search_with_sorting.send_filter()
    search_with_sorting.sort_check()
    assert search_with_sorting.get_results_count() >= min_count
