from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class HandlersNewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'New Window')]"

    NEW_WINDOW_LOC = '//h3'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Handlers_new_window"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="HandlersNewWindowPage -> title")

        self.new_window_element = WebElement(self.browser, self.NEW_WINDOW_LOC,
                                             description="HandlersNewWindowPage -> New Window WebElement")

    def get_text_new_window(self, title):
        Logger.info(f"{self.name} get text new window")
        self.browser.switch_to_window(title)
        return self.new_window_element.get_text()
