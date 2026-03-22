from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class AlertsContextClickPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'Context Menu')]"

    BOX_LOC = 'hot-spot'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "AlertsContextClick"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="AlertsContextClickPage -> title")

        self.box_element = WebElement(self.browser, self.BOX_LOC, description="AlertsPage -> Result WebElement")

    def click_on_the_box(self):
        Logger.info(f"{self.name} click on the box")
        box = self.box_element.wait_for_visible()
        Logger.info(f"{self.name} using ActionChains with the original driver")
        actions = ActionChains(self.browser.driver)
        Logger.info(f"{self.name} move to element box, click")
        actions.move_to_element(box).context_click(box).perform()
