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
    BUTTON_LOGIN = (By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS"]')
    LOGIN_INPUT = (By.XPATH, "(//*[@type='text'])[2]")
    PASSWORD_INPUT = (By.XPATH, "//*[@type='password']")
    # тут не хотел завязываться на disabled, думал это не показатель того что отображается элемент загрузки,
    # как будто disabled просто говорит что на кнопку нажать нельзя, считал что именно _2NVQcOnbtdGIu9O-mB9-YE индикатор спинере загрузки
    BUTTON_LOADING = (By.XPATH, '//button[contains(@class, "DjSvCZoKKfoNSmarsEcTS") and @disabled]')
    #в тг писал, решил завязаться на div[5] вместе text
    ERROR_TEXT = (By.XPATH, '//*[@class="ZHRZ8czyqs7NaNmv65ARI"]//form//div[5]')


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
    time.sleep(1)

    assert text_error.text == error

"""
я понимаю что код выше убог, но как будто иначе никак. Без time.sleep не обойтись потому что
питон работает быстрее чем браузер отрисовывает буквы - пока слип не добавил
ничего не получалось. без него сравниваем " " == error

Но sleep использовать нельзя по сути это плохой знак.

можно конечно вместо sleep написать доп проверку что .text!=" " но это награмаждает.

конкретно тут я бы предложил оставить как было
"""





