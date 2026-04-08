import time

from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.handlers_page import HandlersPage
from pages.handlers_new_window_page import HandlersNewWindowPage
from utils.config_reader import ConfigReader


def test_handlers(browser):
    wait_text_new_window = "New window"
    wait_title_new_window = "New Window"

    Logger.info("Подготовка Handlers")
    handlers = HandlersPage(browser)
    handlers_new_window = HandlersNewWindowPage(browser)
    config = ConfigReader()
    link_handlers = config.get("link_handlers")

    browser.get(link_handlers)
    handlers.wait_for_open()

    handlers.click_new_window()
    handles = browser.driver.window_handles
    browser.driver.switch_to.window(handles[-1])
    title_new_window_1 = browser.driver.title
    text_new_window_1 = handlers_new_window.get_text_new_window(title_new_window_1)
    assert wait_text_new_window == text_new_window_1, f"Ожидаемый текст:{wait_text_new_window}, фактический: {text_new_window_1}"
    assert wait_title_new_window == title_new_window_1, f"Ожидаемый title:{wait_title_new_window}, фактический: {title_new_window_1}"

    browser.switch_to_default_window()
    handlers.wait_for_open()

    handlers.click_new_window()
    handles = browser.driver.window_handles
    browser.driver.switch_to.window(handles[-1])
    title_new_window_2 = browser.driver.title
    text_new_window_2 = handlers_new_window.get_text_new_window(title_new_window_2)
    assert wait_text_new_window == text_new_window_2, f"Ожидаемый текст:{wait_text_new_window}, фактический: {text_new_window_2}"
    assert wait_title_new_window == title_new_window_2, f"Ожидаемый title:{wait_title_new_window}, фактический: {title_new_window_2}"

    browser.switch_to_default_window()
    handlers.wait_for_open()

    browser.driver.switch_to.window(handles[-2])
    browser.close()
    browser.switch_to_default_window()
    browser.driver.switch_to.window(handles[-1])
    browser.close()
    browser.switch_to_default_window()
