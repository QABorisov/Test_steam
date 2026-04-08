from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.actions_page import ActionsPage
from utils.config_reader import ConfigReader
import random


def test_actions(browser):
    Logger.info("Подготовка Actions")
    config = ConfigReader()
    link_actions = config.get("link_actions")
    actions = ActionsPage(browser)

    browser.get(link_actions)
    actions.wait_for_open()

    min_slider = actions.get_min_slider()
    max_slider = actions.get_max_slider()
    value_for_slider = random.randint(min_slider, max_slider)
    step = float(actions.get_step_slider())

    actions.set_slider_value(value_for_slider, step)
    value_slider = actions.get_result_slider()

    wait_value_slider = float(value_for_slider * step)
    assert wait_value_slider == value_slider, f"Ожидаемое значение slider:{wait_value_slider}, фактическое: {value_slider}"
