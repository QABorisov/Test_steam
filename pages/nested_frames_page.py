from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.web_elements import WebElements
from logger.logger import Logger
from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[@id="framesWrapper"]//*[contains(text(), "Nested Frames")]'

    PARENT_FRAME_LOC = 'frame1'
    CHILD_FRAME_LOC = '//iframe'
    TEXT_PARENT_FRAME = '//*[contains(text(), "Parent frame")]'
    TEXT_CHILD_FRAME = '//*[contains(text(), "Child Iframe")]'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "NestedFrames"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="NestedFramesPage -> title")

        self.parent_frame_element = WebElement(self.browser, self.PARENT_FRAME_LOC,
                                               description="NestedFramesPage -> Parent Frame WebElement")
        self.child_frame_element = WebElement(self.browser, self.CHILD_FRAME_LOC,
                                              description="NestedFramesPage -> Child Frame WebElement")
        self.text_parent_frame_element = WebElement(self.browser, self.TEXT_PARENT_FRAME,
                                                    description="NestedFramesPage -> Text Parent Frame WebElement")
        self.text_child_frame_element = WebElement(self.browser, self.TEXT_CHILD_FRAME,
                                                   description="NestedFramesPage -> Text Child Frame WebElement")

    def get_text_parent_frame(self):
        Logger.info(f"{self.name} get text parent frame")
        self.browser.switch_to_frame(self.parent_frame_element)
        text_parent_frame = self.text_parent_frame_element.get_text()
        Logger.info(f"{self.name} switch to default content by original driver")
        self.browser.driver.switch_to.default_content()
        return text_parent_frame

    def get_text_child_frame(self):
        Logger.info(f"{self.name} get text child frame")
        self.browser.switch_to_frame(self.parent_frame_element)
        self.browser.switch_to_frame(self.child_frame_element)
        text_child_frame = self.text_child_frame_element.get_text()
        Logger.info(f"{self.name} switch to default content by original driver")
        self.browser.driver.switch_to.default_content()
        return text_child_frame
