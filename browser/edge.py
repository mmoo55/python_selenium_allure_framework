import edgedriver_autoinstaller
from selenium import webdriver

class Edge:

    def __init__(self):
        edgedriver_autoinstaller.install()

    def iniciar_edge(self):
        """
        Abre el navegador Edge
        :return: webdriver
        """
        driver = webdriver.Edge()
        driver.implicitly_wait(15)
        driver.set_page_load_timeout(15)
        return driver