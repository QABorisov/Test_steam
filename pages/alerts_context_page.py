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
        box = self.box_element.wait_for_presence()
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(box).context_click(box).perform()

    def get_alert_text(self):
        Logger.info(f"{self.name} get alert text")
        return self.browser.get_alert_text()

    def close_alert(self):
        Logger.info(f"{self.name} alert close")
        self.browser.accept_alert()
        self.browser.wait_alert_close()
