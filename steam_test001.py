from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_steam():
    link = "https://store.steampowered.com/"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    registration = browser.find_element(By.XPATH, "//a[text()='вход']")
    registration.click()

    url = "https://store.steampowered.com/login/?redir=&redir_ssl=1"

    assert browser.current_url == url

    login = browser.find_elements(By.XPATH, "//input[@class='_2GBWeup5cttgbTw8FM3tfx']")
    for i in login:
        i.send_keys("Vayaaa")

    button = browser.find_element(By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS"]')
    button.click()
    loading_button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS _2NVQcOnbtdGIu9O-mB9-YE"]'))
    )
    assert loading_button.is_displayed(), "Анимация загрузки не появилась"

    text = "Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова."
    text_error = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@class="_1W_6HXiG4JJ0By1qN_0fGZ"]'), text)
    )

    spiner_button = WebDriverWait(browser, 10).until(
        EC.invisibility_of_element_located(
            (By.XPATH, '//button[@class="DjSvCZoKKfoNSmarsEcTS _2NVQcOnbtdGIu9O-mB9-YE"]'))
    )

