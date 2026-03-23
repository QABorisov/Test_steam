from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.hovers_page import HoversPage
from utils.config_reader import ConfigReader


def test_hovers():
    wait_name_user1 = "user1"
    wait_name_user2 = "user2"
    wait_name_user3 = "user3"

    Logger.info("Подготовка Hovers")
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    hovers = HoversPage(browser)
    config = ConfigReader()
    link_hovers = config.get("link_hovers")

    browser.get(link_hovers)
    hovers.wait_for_open()

    hovers.hover_over_user_1()
    name_user1 = hovers.get_name_user1().replace("name: ", "")
    assert wait_name_user1 == name_user1, f"Ожидаемое имя:{wait_name_user1}, фактическое: {name_user1}"
    hovers.follow_link_user1()
    Logger.info("Возврат браузера на предыдущую страницу")
    browser.driver.back()
    hovers.wait_for_open()

    # я понимаю, что вряд ли требовалось реализовать через дублирование кода, но там страница с юзером не открывалась,
    # решил что пока оставлю так после ревью поправлю если нужно
    hovers.hover_over_user_2()
    name_user2 = hovers.get_name_user2().replace("name: ", "")
    assert wait_name_user2 == name_user2, f"Ожидаемое имя:{wait_name_user2}, фактическое: {name_user2}"
    hovers.follow_link_user2()
    Logger.info("Возврат браузера на предыдущую страницу")
    browser.driver.back()
    hovers.wait_for_open()

    hovers.hover_over_user_3()
    name_user3 = hovers.get_name_user3().replace("name: ", "")
    assert wait_name_user3 == name_user3, f"Ожидаемое имя:{wait_name_user3}, фактическое:{name_user3}"
    hovers.follow_link_user3()
    Logger.info("Возврат браузера на предыдущую страницу")
    browser.driver.back()
    hovers.wait_for_open()
