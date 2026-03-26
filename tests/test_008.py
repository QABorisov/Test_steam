import time

from logger.logger_config import LoggerConfig
from logger.logger import Logger
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from pages.iframe_page import IFrameLeftPanelPage
from pages.nested_frames_page import NestedFramesPage
from pages.frames_page import FramesPage
from utils.config_reader import ConfigReader


def test_iframe(browser):
    wait_text_nested_frames_parent = "Parent frame"
    wait_text_nested_frames_child = "Child Iframe"

    Logger.info("Подготовка Iframe")
    iframelefpanel = IFrameLeftPanelPage(browser)
    nested_frames = NestedFramesPage(browser)
    frames = FramesPage(browser)

    config = ConfigReader()
    link_iframes = config.get("link_iframe")

    browser.get(link_iframes)
    iframelefpanel.wait_for_open()
    iframelefpanel.click_nested_frames()

    nested_frames.wait_for_open()
    text_parent_frame = nested_frames.get_text_parent_frame()
    text_child_frame = nested_frames.get_text_child_frame()

    assert wait_text_nested_frames_parent == text_parent_frame, f"Ожидаемый текст parent:{wait_text_nested_frames_parent}, фактический: {text_parent_frame}"
    assert wait_text_nested_frames_child == text_child_frame, f"Ожидаемый текст child:{wait_text_nested_frames_child}, фактический: {text_child_frame}"

    # browser.get(link_iframes)
    iframelefpanel.click_frames()
    # вот ошибка тут я хоть убей не могу кликнуть, точнее кликаю но не работает
    frames.wait_for_open()

    text_top_frames = frames.get_text_top_frame()
    text_bottom_frames = frames.get_text_bottom_frame()

    assert text_top_frames == text_bottom_frames, f"Текст top frames:{text_top_frames}, Текст bottom frames: {text_bottom_frames}, ожидаем =="
