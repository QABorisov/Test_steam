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

def test_steam(browser):
    LINK = "https://store.steampowered.com/"
    TIMEOUT=5
    fake_ru = Faker('ru_RU')

    browser.get(LINK)

    registration = WebDriverWait(browser, TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='вход']"))
    )
    registration.click()

    button=WebDriverWait(browser, TIMEOUT).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS"]'))
    )

    assert button.is_displayed()


    login = WebDriverWait(browser, TIMEOUT).until(
        EC.visibility_of_element_located((By.XPATH, "(//*[@type='text'])[2]"))
    )
    login.send_keys(fake_ru.email())

    password=WebDriverWait(browser, TIMEOUT).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@type='password']"))
    )
    password.send_keys(fake_ru.password())

    button_log_in = WebDriverWait(browser, TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS"]'))
    )
    button_log_in.click()


    loading_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS _2NVQcOnbtdGIu9O-mB9-YE"]'))
    )
    assert loading_button.is_displayed(), "Анимация загрузки не появилась"

    error = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    text_error = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located ((By.XPATH, f'//*[text()="{error}"]'))

    )

    spiner_button = WebDriverWait(browser, 10).until_not(
        EC.visibility_of_element_located(
            (By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS _2NVQcOnbtdGIu9O-mB9-YE"]'))
    )
