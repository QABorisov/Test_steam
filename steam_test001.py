import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from faker import Faker


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


class SteamConstant:
    LINK = "https://store.steampowered.com/"
    TIMEOUT = 5

    REGISTRATION_LINK = (By.XPATH, "//a[text()='вход']")
    BUTTON_LOGIN = (By.XPATH, '(//button[@type="submit"])[2]')
    LOGIN_INPUT = (By.XPATH, "(//*[@type='text'])[2]")
    PASSWORD_INPUT = (By.XPATH, "//*[@type='password']")
    BUTTON_LOADING = (By.XPATH, '//button[contains(@type, "submit") and @disabled]')
    ERROR_TEXT = (By.XPATH, '//*[@id="responsive_page_template_content"]//form//div[5]')

def sleep(element):
    poll_interval = 0.5
    start=time.time()

    while True:
        result=element.text.strip()
        if result!="":
            break
        if time.time()-start > SteamConstant.TIMEOUT:
            raise TimeoutError("Текст ошибки не появился")
        time.sleep(poll_interval)


def test_steam(browser):
    fake_ru = Faker('ru_RU')
    browser.get(SteamConstant.LINK)
    error = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."

    registration = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.element_to_be_clickable(SteamConstant.REGISTRATION_LINK)
    )
    registration.click()

    button = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.visibility_of_element_located(SteamConstant.BUTTON_LOGIN)
    )

    login = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.visibility_of_element_located(SteamConstant.LOGIN_INPUT)
    )
    login.send_keys(fake_ru.email())

    password = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.visibility_of_element_located(SteamConstant.PASSWORD_INPUT)
    )
    password.send_keys(fake_ru.password())

    button_log_in = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.element_to_be_clickable(SteamConstant.BUTTON_LOGIN)
    )
    button_log_in.click()

    loading_button = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.visibility_of_element_located(SteamConstant.BUTTON_LOADING)
    )
    assert loading_button.is_displayed(), "Анимация загрузки не появилась"

    spiner_button = WebDriverWait(browser, SteamConstant.TIMEOUT).until_not(
        EC.visibility_of_element_located(
            SteamConstant.BUTTON_LOADING)
    )
    text_error = WebDriverWait(browser, SteamConstant.TIMEOUT).until(
        EC.visibility_of_element_located(SteamConstant.ERROR_TEXT)
    )
    sleep(text_error)
    #добавил функцию sleep по статье, но как назло стало работать и без всяких слипов

    assert text_error.text == error, f"Ожидаемый результат: {error}. Фактичсекий: {text_error.text}"





