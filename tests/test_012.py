from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.upload_image_page import UploadImagePage
from utils.config_reader import ConfigReader
import os
from pages.pyautogui_utilities import PyAutoGUIUtilities


def test_upload_image_and_dialog_window(browser):
    wait_file_name = "image_cat.png"
    path_file = os.path.abspath(wait_file_name)

    Logger.info("Подготовка Upload Image + dialog window")
    upload = UploadImagePage(browser)
    py_auto_gui = PyAutoGUIUtilities()

    config = ConfigReader()
    link_upload = config.get("link_upload_image")

    browser.get(link_upload)
    upload.wait_for_open()

    upload.click_area()
    py_auto_gui.upload_file(path_file)

    file_name = upload.get_file_name_area()
    assert wait_file_name == file_name, f"Ожидаемое имя файла:{wait_file_name}, фактическое: {file_name}"
