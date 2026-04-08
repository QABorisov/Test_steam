import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory

@pytest.fixture
def browser():
    docker_options = ["--headless", "--no-sandbox", "--disable-dev-shm-usage", "--window-size=1920,1080"]
    driver = BrowserFactory.get_driver(options=docker_options)
    browser = Browser(driver)
    yield browser
    browser.quit()