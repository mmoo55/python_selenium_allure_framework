import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Headless:

    def __init__(self):
        chromedriver_autoinstaller.install()

    def iniciar_headless(self):
        """
        Abre el navegador Chrome en modo Headless
        :return: webdriver
        """
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(15)
        return driver