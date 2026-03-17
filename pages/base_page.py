from browser.browser import Browser
from logger.logger import Logger


class BasePage:
    UNIQUE_ELEMENT_LOC = None
    LINK = None

    def __init__(self, browser: Browser):
        self.browser = browser
        self.page_name = None
        self.unique_element = None

    def wait_for_open(self) -> None:
        Logger.info(f"{self}: wait for open")
        self.unique_element.wait_for_presence()

    def load_page(self) -> None:
        Logger.info(f"{self}: load_page {self.LINK}")
        self.browser.get(self.LINK)

    def __str__(self):
        return f"{self.__class__.__name__}[{self.page_name}]"

    def __repr__(self):
        return str(self)
