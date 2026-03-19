from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from logger.logger import Logger
from pages.base_page import BasePage


class AlertsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'JavaScript Alerts')]"
    ALERT_LOC = '//*[@onclick="jsAlert()"]'
    CONFIRM_LOC = '//*[@onclick="jsConfirm()"]'
    PROMT_LOC = '//*[@onclick="jsPrompt()"]'
    RESULT_LOC = "result"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "Alerts"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC, description="AlertsPage -> title")

        self.alert_button = Button(self.browser, self.ALERT_LOC, description="AlertsPage -> Alert button")
        self.confirm_button = Button(self.browser, self.CONFIRM_LOC, description="AlertsPage -> Confirm button")
        self.promt_button = Button(self.browser, self.PROMT_LOC, description="AlertsPage -> Promt button")
        self.result_element = WebElement(self.browser, self.RESULT_LOC, description="AlertsPage -> Result WebElement")

    def click_and_close_alert(self):
        Logger.info(f"{self.name} click and close alert")
        self.alert_button.click()
        text_alert = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text_alert

    def click_js_and_close_alert(self):
        Logger.info(f"{self.name} click js and close alert")
        self.alert_button.js_click()
        text_alert = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text_alert

    def click_and_close_confirm(self):
        Logger.info(f"{self.name} click and close confirm")
        self.confirm_button.click()
        text_confirm = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text_confirm

    def click_js_and_close_confirm(self):
        Logger.info(f"{self.name} click and close confirm")
        self.confirm_button.js_click()
        text_confirm = self.browser.get_alert_text()
        self.browser.accept_alert()
        return text_confirm

    def click_promt(self):
        Logger.info(f"{self.name} click and close promt")
        self.promt_button.click()
        text_promt = self.browser.get_alert_text()
        return text_promt

    def click_js_promt(self):
        Logger.info(f"{self.name} click and close promt")
        self.promt_button.js_click()
        text_promt = self.browser.get_alert_text()
        return text_promt

    def send_keys_promt(self, word):
        Logger.info(f"{self.name} send keys promt {word}")
        self.browser.send_keys_alert(word)
        self.browser.accept_alert()

    def get_text_result(self):
        Logger.info(f"{self.name} get text result")
        return self.result_element.get_text()
