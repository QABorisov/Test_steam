from elements.base_element import BaseElement
from logger.logger import Logger
from browser.browser import Browser
from selenium.common import WebDriverException
from logger.logger import Logger


class Input(BaseElement):
    def clear(self) -> None:
        element = self.wait_for_visible()
        Logger.info(f"{self}: clear")
        try:
            element.clear()
        except WebDriverException as err:
            Logger.error(f"{self} {err}")
            raise

    def send_keys(self, keys: str, clear: bool = True) -> None:
        if clear:
            self.clear()
        element = self.wait_for_visible()
        Logger.info(f"{self} send keys={keys}")
        try:
            element.send_keys(keys)
        except WebDriverException as err:
            Logger.error(f"{self} {err}")
            raise
