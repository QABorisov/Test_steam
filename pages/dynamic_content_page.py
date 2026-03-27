from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Dynamic Content')]"

    IMAGES_LOC = '(//*[@id="content"]//img)[{}]'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "DynamicContent"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="DynamicContentPage -> title")

        self.images_multi_web_elements = MultiWebElement(self.browser, self.IMAGES_LOC,
                                                         description="DynamicContentPage -> images MultiWebElement")

    def get_list_link_img(self):
        Logger.info(f"{self.name} get link img")
        list_img = []
        for i in list(self.images_multi_web_elements):
            list_img.append(i.get_attribute("src"))
        return list_img
