from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage


class IFrameLeftPanelPage(BasePage):
    UNIQUE_ELEMENT_LOC = '//*[@class="left-pannel"]'

    ALERT_FRAME_WINDOW_LOC = '//*[@class="element-group"][3]//*[@class="header-wrapper"]'
    NESTED_FRAMES_LOC = '//*[@class="element-group"][3]//*[@id="item-3"]'
    FRAMES_LOC = '//*[@class="element-group"][3]//*[@id="item-2"]//a'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "IFrameLeftPanel"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="IFrameLeftPanelPage -> Left panel element")
        self.alert_frame_window_button = Button(self.browser, self.ALERT_FRAME_WINDOW_LOC,
                                                description="IFrameLeftPanelPage -> Alert Frame Window Button")
        self.nested_button = Button(self.browser, self.NESTED_FRAMES_LOC,
                                    description="IFrameLeftPanelPage -> Nested Button")
        self.frames_button = Button(self.browser, self.FRAMES_LOC,
                                    description="IFrameLeftPanelPage -> Frames Button")

    def click_nested_frames(self):
        Logger.info(f"{self.name} click alert frame window and nested frames")
        self.alert_frame_window_button.js_click()
        self.alert_frame_window_button.js_click()
        self.nested_button.click()

    def click_frames(self):
        self.frames_button.js_click()
