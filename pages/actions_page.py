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

    def set_slider_value(self, value, step):
        Logger.info(f"{self.name} set slider value: {value}")
        slider = self.slider_input.wait_for_clickable()
        current_value = float(self.result_slider_element.get_text())
        key_to_send = Keys.ARROW_RIGHT if value * step > current_value else Keys.ARROW_LEFT
        slider.send_keys(key_to_send * value)
        # я реализовал как ты просишь, но не совсем согласен, чтобы понять в какую сторону двигать
        # приходится завязаться на self.result_slider_element, но это нелогично ведь нам его и нужно проверить это ведь цель кейса

    def get_min_slider(self):
        min_slider = int(float(self.slider_input.get_attribute("min")))
        return min_slider

    def get_max_slider(self):
        max_slider = int(float(self.slider_input.get_attribute("max")))
        return max_slider

    def get_step_slider(self):
        step = self.slider_input.get_attribute("step")
        return step

    def get_result_slider(self):
        return float(self.result_slider_element.get_text())
