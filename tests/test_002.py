from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.alerts_page import AlertsPage
from faker import Faker
from utils.config_reader import ConfigReader


def test_alerts(browser):
    wait_text_alert = "I am a JS Alert"
    wait_result_alert = "You subccessfuly clicked an alert"
    wait_text_confirm = "I am a JS Confirm"
    wait_result_confirm = "You clicked: Ok"
    wait_text_promt = "I am a JS Prompt"
    wait_result_promt = "You entered: "

    Logger.info("Подготовка alerts")
    alerts = AlertsPage(browser)
    config = ConfigReader()
    link_alerts = config.get("link_alerts")

    browser.get(link_alerts)
    alerts.wait_for_open()

    text_alert = alerts.click_and_close_alert()
    assert wait_text_alert == text_alert, f"Ожидаемый текст alert:{wait_text_alert}, фактический: {text_alert}"
    text_result_alert = alerts.get_text_result()
    assert wait_result_alert == text_result_alert, f"Ожидаемый текст alert:{wait_result_alert}, фактический: {text_result_alert}"

    text_confirm = alerts.click_and_close_confirm()
    assert wait_text_confirm == text_confirm, f"Ожидаемый текст alert:{wait_text_confirm}, фактический: {text_confirm}"
    text_result_confirm = alerts.get_text_result()
    assert wait_result_confirm == text_result_confirm, f"Ожидаемый текст alert:{wait_result_confirm}, фактический: {text_result_confirm}"

    text_promt = alerts.click_promt()
    assert wait_text_promt == text_promt, f"Ожидаемый текст alert:{wait_text_promt}, фактический: {text_promt}"
    fake = Faker()
    random_word = fake.word()
    alerts.send_keys_promt(random_word)
    text_result_promt = alerts.get_text_result()
    assert wait_result_promt + random_word == text_result_promt, f"Ожидаемый текст alert:{wait_result_promt}{random_word}, фактический: {text_result_promt}"
