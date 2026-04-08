from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Hovers')]"

    COUNT_USERS_LOC = '//*[contains(@class,"figure")][{}]'
    USER_BY_INDEX_LOC = '//*[contains(@class,"figure")][{}]'
    USER_NAME_BY_INDEX_LOC = '//*[contains(@class,"figure")][{}]//h5'
    USER_LINK_BY_INDEX_LOC = '//*[contains(@class,"figure")][{}]//*[contains(text(), "View profile")]'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Hovers"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="HoversPage -> title")

        self.count_users_element = MultiWebElement(self.browser, self.COUNT_USERS_LOC,
                                                   description="HoversPage -> Count users elements")

    def get_count_users(self):
        Logger.info(f"{self.name} get count users by MultiWebElement")
        users_list = list(self.count_users_element)
        return len(users_list)

    def hover_over_user(self, index):
        Logger.info(f"{self.name} hover over user {index}")

        dynamic_xpath = self.USER_BY_INDEX_LOC.format(index)
        user_element = WebElement(self.browser, dynamic_xpath, description=f"HoversPage -> User {index} Element")

        user = user_element.wait_for_visible()
        Logger.info(f"{self.name} using ActionChains with the original driver")
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(user).perform()

    def get_name_user(self, index):
        Logger.info(f"{self.name} get name user {index}")

        dynamic_xpath = self.USER_NAME_BY_INDEX_LOC.format(index)
        user_name_label = Label(self.browser, dynamic_xpath, description=f"HoversPage -> User {index} name Label")

        return user_name_label.get_text()

    def follow_link_user(self, index):
        Logger.info(f"{self.name} follow link user {index}")

        dynamic_xpath = self.USER_LINK_BY_INDEX_LOC.format(index)
        user_name_label = Button(self.browser, dynamic_xpath, description=f"HoversPage -> User {index} Link")

        user_name_label.click()
