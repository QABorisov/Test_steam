from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage


class FramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[@id="framesWrapper"]//*[text()="Frames"]'

    TOP_FRAME_LOC = 'frame1'
    BOTTOM_FRAME_LOC = 'frame2'
    TEXT_TOP_FRAME = 'sampleHeading'
    TEXT_BOTTOM_FRAME = 'sampleHeading'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Frames"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="FramesPage -> title")

        self.top_frame_element = WebElement(self.browser, self.TOP_FRAME_LOC,
                                            description="FramesPage -> Top Frame WebElement")
        self.bottom_frame_element = WebElement(self.browser, self.BOTTOM_FRAME_LOC,
                                               description="FramesPage -> Bottom Frame WebElement")
        self.text_top_frame_element = WebElement(self.browser, self.TEXT_TOP_FRAME,
                                                 description="FramesPage -> Text Top Frame WebElement")
        self.text_bottom_frame_element = WebElement(self.browser, self.TEXT_BOTTOM_FRAME,
                                                    description="FramesPage -> Text Bottom Frame WebElement")

    def get_text_top_frame(self):
        Logger.info(f"{self.name} get text top frame")
        self.browser.switch_to_frame(self.top_frame_element)
        text_top_frame = self.text_top_frame_element.get_text()
        Logger.info(f"{self.name} switch to default content by original driver")
        self.browser.driver.switch_to.default_content()
        return text_top_frame

    def get_text_bottom_frame(self):
        Logger.info(f"{self.name} get text bottom frame")
        self.browser.switch_to_frame(self.bottom_frame_element)
        text_bottom_frame = self.text_bottom_frame_element.get_text()
        Logger.info(f"{self.name} switch to default content by original driver")
        self.browser.driver.switch_to.default_content()
        return text_bottom_frame
