from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.dynamic_content_page import DynamicContentPage
from utils.config_reader import ConfigReader


def test_dynamic_content(browser):
    Logger.info("Подготовка Dynamic Content")
    dynamic_content = DynamicContentPage(browser)
    config = ConfigReader()
    link_dynamic_content = config.get("link_dynamic_content")

    browser.get(link_dynamic_content)
    dynamic_content.wait_for_open()

    while True:
        list_img = dynamic_content.get_list_link_img()
        set_img = set(list_img)
        if len(list_img) == len(set_img):
            browser.driver.refresh()
        else:
            break
