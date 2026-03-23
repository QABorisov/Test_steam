from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class HandlersPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Opening a new window')]"

    CLICK_LOC = '//*[contains(text(), "Click Here")]'
    NEW_WINDOW_LOC = '//h3'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Handlers"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="HandlersPage -> title")

        self.click_button = Button(self.browser, self.CLICK_LOC, description="HandlersPage -> Click Button")
        self.new_window_element = WebElement(self.browser, self.NEW_WINDOW_LOC,
                                             description="HandlersPage -> New Window WebElement")

    def click_new_window(self):
        Logger.info(f"{self.name} click new window")
        self.click_button.click()

    def get_text_new_window(self, title):
        Logger.info(f"{self.name} get text new window")
        self.browser.switch_to_window(title)
        return self.new_window_element.get_text()

    def get_title(self):
        Logger.info(f"{self.name} get title using original browser")
        return self.browser.driver.title
