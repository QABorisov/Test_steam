from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class HoversPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Hovers')]"

    USER_1_LOC = '//*[@class="figure"][1]'
    USER_2_LOC = '//*[@class="figure"][2]'
    USER_3_LOC = '//*[@class="figure"][3]'
    USER_1_NAME_LOC = '//*[@class="figure"][1]//h5'
    USER_2_NAME_LOC = '//*[@class="figure"][2]//h5'
    USER_3_NAME_LOC = '//*[@class="figure"][3]//h5'
    USER_1_LINK_LOC = '//*[@class="figure"][1]//*[contains(text(), "View profile")]'
    USER_2_LINK_LOC = '//*[@class="figure"][2]//*[contains(text(), "View profile")]'
    USER_3_LINK_LOC = '//*[@class="figure"][3]//*[contains(text(), "View profile")]'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Hovers"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="HoversPage -> title")

        self.user_1_element = WebElement(self.browser, self.USER_1_LOC, description="HoversPage -> User 1 Element")
        self.user_2_element = WebElement(self.browser, self.USER_2_LOC, description="HoversPage -> User 2 Element")
        self.user_3_element = WebElement(self.browser, self.USER_3_LOC, description="HoversPage -> User 3 Element")

        self.user_1_name_element = WebElement(self.browser, self.USER_1_NAME_LOC,
                                              description="HoversPage -> User1 name Element")
        self.user_2_name_element = WebElement(self.browser, self.USER_2_NAME_LOC,
                                              description="HoversPage -> User2 name Element")
        self.user_3_name_element = WebElement(self.browser, self.USER_3_NAME_LOC,
                                              description="HoversPage -> User3 name Element")

        self.user_1_button = Button(self.browser, self.USER_1_LINK_LOC, description="HoversPage -> User 1 Link")
        self.user_2_button = Button(self.browser, self.USER_2_LINK_LOC, description="HoversPage -> User 2 Link")
        self.user_3_button = Button(self.browser, self.USER_3_LINK_LOC, description="HoversPage -> User 3 Link")

    def hover_over_user_1(self):
        Logger.info(f"{self.name} hover over user 1")
        user = self.user_1_element.wait_for_visible()
        Logger.info(f"{self.name} using ActionChains with the original driver")
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(user).perform()

    def get_name_user1(self):
        Logger.info(f"{self.name} get name user1")
        return self.user_1_name_element.get_text()

    def follow_link_user1(self):
        Logger.info(f"{self.name} follow link user1")
        self.user_1_button.click()

    def hover_over_user_2(self):
        Logger.info(f"{self.name} hover over user 2")
        user = self.user_2_element.wait_for_visible()
        Logger.info(f"{self.name} using ActionChains with the original driver")
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(user).perform()

    def get_name_user2(self):
        Logger.info(f"{self.name} get name user2")
        return self.user_2_name_element.get_text()

    def follow_link_user2(self):
        Logger.info(f"{self.name} follow link user2")
        self.user_2_button.click()

    def hover_over_user_3(self):
        Logger.info(f"{self.name} hover over user 3")
        user = self.user_3_element.wait_for_visible()
        Logger.info(f"{self.name} using ActionChains with the original driver")
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(user).perform()

    def get_name_user3(self):
        Logger.info(f"{self.name} get name user3")
        return self.user_3_name_element.get_text()

    def follow_link_user3(self):
        Logger.info(f"{self.name} follow link user3")
        self.user_3_button.click()
