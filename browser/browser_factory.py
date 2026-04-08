from enum import StrEnum
from selenium import webdriver
from logger.logger import Logger


class DriverName(StrEnum):
    CHROME = "chrome"


class BrowserFactory():
    @staticmethod
    def get_driver(
            driver_name: DriverName = DriverName.CHROME,
            options: list[str] = None):
        if options is None:
            options = []
        Logger.info(f"Start webdriver: {driver_name}, options: {options}")
        if driver_name == DriverName.CHROME:
            chrome_options = webdriver.ChromeOptions()

            for option in options:
                chrome_options.add_argument(option)
            driver = webdriver.Chrome(options=chrome_options)
        else:
            raise NotImplementedError(f"driver_name={driver_name} not emplementing")
        return driver
