from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.hovers_page import HoversPage
from utils.config_reader import ConfigReader


def test_hovers(browser):
    Logger.info("Подготовка Hovers")
    hovers = HoversPage(browser)
    config = ConfigReader()
    link_hovers = config.get("link_hovers")

    browser.get(link_hovers)
    hovers.wait_for_open()

    users = hovers.get_count_users()

    for i in range(1, users + 1):
        wait_name_user = "user"
        hovers.hover_over_user(i)
        name_user = hovers.get_name_user(i).replace("name: ", "")
        wait_name_user += str(i)
        assert wait_name_user == name_user, f"Ожидаемое имя:{wait_name_user}, фактическое: {name_user}"
        hovers.follow_link_user(i)
        Logger.info("Возврат браузера на предыдущую страницу")
        browser.go_back()
        hovers.wait_for_open()
