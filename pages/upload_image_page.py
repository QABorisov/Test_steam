from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage
import os
from selenium.webdriver.common.action_chains import ActionChains


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'File Uploader')]"

    UPLOAD_LOC = 'file-upload'
    UPLOAD_BUTTON_LOC = 'file-submit'
    UPLOADED_LOC = "//h3[contains(text(), 'File Uploaded!')]"
    FILE_NAME_LOC = "uploaded-files"
    LOADING_AREA_LOC = "drag-drop-upload"
    FILE_NAME_AREA_LOC = '(//*[@id="drag-drop-upload"]//span)[1]'
    CHECK_MARK_LOC = '(//*[@id="drag-drop-upload"]//span)[2]'

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "UploadImage"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="UploadImagePage -> title")

        self.upload_input = Input(self.browser, self.UPLOAD_LOC,
                                  description="UploadImagePage ->Upload Input")
        self.select_file_button = Button(self.browser, self.UPLOAD_LOC,
                                  description="UploadImagePage ->Select File Button")

        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON_LOC,
                                    description="UploadImagePage ->Upload Button")
        self.uploaded_element = WebElement(self.browser, self.UPLOADED_LOC,
                                           description="UploadImagePage ->Uploaded title")

        self.file_name_element = WebElement(self.browser, self.FILE_NAME_LOC,
                                            description="UploadImagePage ->File Name Element")

        self.loading_area_input = Input(self.browser, self.LOADING_AREA_LOC,
                                        description="UploadImagePage ->Loading Area Input")
        self.file_name_area_element = WebElement(self.browser, self.FILE_NAME_AREA_LOC,
                                                 description="UploadImagePage ->File Name Area Element")
        self.check_mark_element = WebElement(self.browser, self.CHECK_MARK_LOC,
                                             description="UploadImagePage ->Check Mark Element")

    def upload_image(self, path_file):
        Logger.info(f"{self.name} upload image")
        self.upload_input.send_keys(path_file)
        self.upload_button.click()

    def get_file_name(self):
        Logger.info(f"{self.name} get file name")
        self.uploaded_element.wait_for_presence()
        file_name = self.file_name_element.get_text()
        return file_name

    def click_area(self):
        Logger.info(f"{self.name} click area")
        element = self.loading_area_input.wait_for_visible()
        actins = ActionChains(self.browser.driver)
        actins.move_to_element(element).click().perform()

    def get_file_name_area(self):
        Logger.info(f"{self.name} get file name area")
        self.check_mark_element.wait_for_presence()
        file_name = self.file_name_area_element.get_text()
        return file_name

    def open_explorer(self):
        Logger.info(f"{self.name} open explorer")
        self.select_file_button.js_click()
