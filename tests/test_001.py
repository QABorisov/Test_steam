from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.basic_auth_page import BasicAuthPage
from utils.config_reader import ConfigReader


def test_basic_auth(browser):
    wait_result_alert = "Congratulations! You must have the proper credentials."

    Logger.info("Подготовка Basic Authorization")
    basic_auth = BasicAuthPage(browser)
    config = ConfigReader()
    link_auth = config.get("basic_authorization")
    user = config.get("user")
    password = config.get("password")
    Logger.info(f"{basic_auth.name} authorization")
    auth_link = link_auth.replace("://", f"://{user}:{password}@")

    browser.get(auth_link)
    basic_auth.wait_for_open()

    text_result_auth = basic_auth.get_text_result()
    assert text_result_auth == wait_result_alert, f"Ожидаемый текст alert:{wait_result_alert}, фактический: {text_result_auth}"
