from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Infinite Scroll')]"

    PARAGRAPHS_LOC = '//*[@class="jscroll-inner"]//*[@class="jscroll-added"][{}]'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "InfinityScroll"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="InfinityScrollPage -> title")

        self.paragraphs_multi_web_elements = MultiWebElement(self.browser, self.PARAGRAPHS_LOC,
                                                             description="InfinityScrollPage -> Paragraphs Multi Web Elements")

    def get_count_paragraphs(self):
        Logger.info(f"{self.name} get count paragraphs")
        paragraphs_list = list(self.paragraphs_multi_web_elements)
        return len(paragraphs_list)
