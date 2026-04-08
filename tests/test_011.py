from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.upload_image_page import UploadImagePage
from utils.config_reader import ConfigReader
import os


def test_upload_image(browser):
    wait_file_name = "image_cat.png"
    path_file = os.path.abspath(wait_file_name)

    Logger.info("Подготовка Upload Image")
    upload = UploadImagePage(browser)

    config = ConfigReader()
    link_upload = config.get("link_upload_image")

    browser.get(link_upload)
    upload.wait_for_open()

    upload.upload_image(path_file)
    file_name = upload.get_file_name()

    assert wait_file_name == file_name, f"Ожидаемое имя файла:{wait_file_name}, фактическое: {file_name}"
