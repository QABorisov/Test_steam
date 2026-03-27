from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.Infinity_scroll_page import InfinityScrollPage
from utils.config_reader import ConfigReader


def test_infinity_scroll(browser):
    tester_years_old = 29

    Logger.info("Подготовка InfinityScroll")
    infinity_scroll = InfinityScrollPage(browser)
    config = ConfigReader()
    link_infinity_scroll = config.get("link_infinity_scroll")

    browser.get(link_infinity_scroll)
    infinity_scroll.wait_for_open()

    while True:
        count = infinity_scroll.get_count_paragraphs()
        if count < tester_years_old:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        else:
            break
