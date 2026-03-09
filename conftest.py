import pytest
from core import BrowserManager


@pytest.fixture(params=["ru", "en"], scope="function")
def browser(request):
    language = request.param
    browser = BrowserManager(language=language)
    yield browser
    BrowserManager.close()
