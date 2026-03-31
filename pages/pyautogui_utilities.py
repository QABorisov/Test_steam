from logger.logger import Logger
import time
import pyautogui
import os
import pygetwindow as gw


class PyAutoGUIUtilities:
    @staticmethod
    def upload_file(path: str) -> None:
        Logger.info("Upload file by PyAutoGUIUtilities")
        time.sleep(3)
        Logger.info(f"Upload file:{path}")
        pyautogui.write(path)
        Logger.info(f"Press Enter")
        pyautogui.press("enter")
        time.sleep(1)

    @staticmethod
    def upload_file_drag_and_drop(path: str, dir_name: str) -> None:
        img_dir = os.path.dirname(path)
        os.startfile(img_dir)
        time.sleep(2)

        window = gw.getWindowsWithTitle(dir_name)[0]
        window.activate()
        time.sleep(1)

        file_pixel = (873, 487)
        drop_pixel = (117, 836)

        Logger.info(f"Перетаскивание из {file_pixel} в {drop_pixel}")

        pyautogui.moveTo(file_pixel, duration=0.5)
        pyautogui.mouseDown(button="left")
        time.sleep(0.5)

        pyautogui.moveTo(drop_pixel, duration=0.7)
        time.sleep(0.3)
        pyautogui.mouseUp(button="left")

        Logger.info("Файл успешно перетащен")
