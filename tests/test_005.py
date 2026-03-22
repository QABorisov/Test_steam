from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.actions_page import ActionsPage
from utils.config_reader import ConfigReader


def test_actions():
    value_for_slider = 5

    Logger.info("Подготовка Actions")
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    actions = ActionsPage(browser)
    config = ConfigReader()
    link_actions = config.get("link_actions")

    browser.get(link_actions)
    actions.wait_for_open()
    actions.set_slider_value(value_for_slider)
    value_slider = actions.get_result_slider()
    step = float(actions.get_step_slider())
    wait_value_slider = str(value_for_slider * step)
    assert wait_value_slider == value_slider, f"Ожидаемое значение slider:{wait_value_slider}, фактическое: {value_slider}"
