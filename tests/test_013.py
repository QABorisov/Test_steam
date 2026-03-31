from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.upload_image_page import UploadImagePage
from utils.config_reader import ConfigReader
import os
from pages.pyautogui_utilities import PyAutoGUIUtilities


def test_upload_drag_and_drop(browser):
    wait_file_name = "image_cat.png"
    dir_name = "image"
    path_file = os.path.abspath(os.path.join(dir_name, wait_file_name))

    Logger.info("Подготовка Upload Image")
    upload = UploadImagePage(browser)
    py_auto_gui = PyAutoGUIUtilities()

    config = ConfigReader()
    link_upload = config.get("link_upload_image")

    browser.get(link_upload)
    upload.wait_for_open()

    upload.open_explorer()

    py_auto_gui.upload_file_drag_and_drop(path_file, dir_name)

    file_name = upload.get_file_name_area()
    assert wait_file_name == file_name, f"Ожидаемое имя файла:{wait_file_name}, фактическое: {file_name}"