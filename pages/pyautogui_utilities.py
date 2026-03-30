from logger.logger import Logger
import time
import pyautogui


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(path: str) -> None:
        Logger.info("Upload file by PyAutoGUIUtilities")
        time.sleep(3)
        Logger.info(f"Upload file:{path}")
        pyautogui.write(path)
        Logger.info(f"Press Enter")
        pyautogui.press("enter")
