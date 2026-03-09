from selenium import webdriver


class BrowserManager:
    _instance = None

    def __new__(cls, language="en"):
        if cls._instance is None:
            options = webdriver.ChromeOptions()
            options.add_argument(f"--lang={language}")
            options.add_experimental_option("prefs", {'intl.accept_languages': language})
            cls._instance = webdriver.Chrome(options=options)
        return cls._instance

    @classmethod
    def close(cls):
        if cls._instance:
            cls._instance.quit()
            cls._instance = None
