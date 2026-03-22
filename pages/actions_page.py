from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class ActionsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Horizontal Slider')]"

    SLIDER_LOC = '//*[@type="range"]'
    RESULT_SLIDER_LOC = 'range'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Actions"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="ActionsPage -> title")

        self.slider_input = Input(self.browser, self.SLIDER_LOC,
                                  description="ActionsPage -> Slider Input")
        self.result_slider_element = WebElement(self.browser, self.RESULT_SLIDER_LOC,
                                                description="ActionsPage -> Result Slider WebElement")

    def set_slider_value(self, value):
        Logger.info(f"{self.name} set slider value: {value}")
        slider = self.slider_input.wait_for_clickable()
        for _ in range(value):
            slider.send_keys(Keys.ARROW_RIGHT)

    def get_step_slider(self):
        Logger.info(f"{self.name} get_step_slider")
        step = self.slider_input.get_attribute("step")
        return step

    def get_result_slider(self):
        Logger.info(f"{self.name} get result slider")
        return self.result_slider_element.get_text()
