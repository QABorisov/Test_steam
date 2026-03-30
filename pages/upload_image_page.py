from elements.button import Button
from elements.input import Input
from elements.label import Label
from elements.web_element import WebElement
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage
import os


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[contains(text(), 'File Uploader')]"

    UPLOAD_LOC = 'file-upload'
    UPLOAD_BUTTON_LOC = 'file-submit'
    UPLOADED_LOC = "//h3[contains(text(), 'File Uploaded!')]"
    FILE_NAME_LOC = "uploaded-files"

    def __init__(self, browser):
        super().__init__(browser)
        self.name = "UploadImage"
        self.unique_element = WebElement(self.browser, self.UNIQUE_ELEMENT_LOC,
                                         description="UploadImagePage -> title")

        self.upload_input = Input(self.browser, self.UPLOAD_LOC,
                                  description="UploadImagePage ->Upload Input")
        self.upload_button = Button(self.browser, self.UPLOAD_BUTTON_LOC,
                                    description="UploadImagePage ->Upload Button")
        self.uploaded_element = WebElement(self.browser, self.UPLOADED_LOC,
                                           description="UploadImagePage ->Uploaded title")

        self.file_name_element = WebElement(self.browser, self.FILE_NAME_LOC,
                                            description="UploadImagePage ->File Name Element")

    def upload_image(self, path):
        Logger.info(f"{self.name} upload image")
        path_file = os.path.abspath(path)
        self.upload_input.send_keys(path_file)
        self.upload_button.click()

    def get_file_name(self):
        Logger.info(f"{self.name} get file name")
        self.uploaded_element.wait_for_presence()
        text = self.file_name_element.get_text()
        return text
