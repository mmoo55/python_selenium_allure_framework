import geckodriver_autoinstaller
from selenium import webdriver

class Firefox:

    def __init__(self):
        geckodriver_autoinstaller.install()

    def iniciar_firefox(self):
        """
        Abre el navegador Firefox
        :return: webdriver
        """
        driver = webdriver.Firefox()
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(15)
        return driver