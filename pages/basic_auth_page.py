from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Basic Auth')]"
    RESULT_LOC = '//*[@id="content"]//p'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "BasicAuth"

        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description="BasicAuthPage -> title")
        self.result_element = WebElement(self.browser, self.RESULT_LOC,
                                         description="BasicAuthPage -> Result WebElement")

    def get_text_result(self):
        return self.result_element.get_text()
