from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.alerts_context_page import AlertsContextClickPage
from utils.config_reader import ConfigReader


def test_alerts_context_click():
    wait_text_alert = "You selected a context menu"

    Logger.info("Подготовка alerts context click")
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    alerts_context = AlertsContextClickPage(browser)
    config = ConfigReader()
    link_alerts_context_click = config.get("link_alerts_context_click")

    browser.get(link_alerts_context_click)
    alerts_context.wait_for_open()
    alerts_context.click_on_the_box()
    text_alert = alerts_context.get_alert_text()
    assert wait_text_alert == text_alert, f"Ожидаемый текст alert:{wait_text_alert}, фактический: {text_alert}"
    alerts_context.close_alert()
