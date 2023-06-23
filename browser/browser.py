from selenium import webdriver

from browser.chrome import Chrome
from browser.edge import Edge
from browser.firefox import Firefox
from browser.headless import Headless


class Browser:

    def __init__(self):
        self.driver = None

    def seleccionar_navegador(self, navigator: str = "chrome"):
        """
        Permite elegir el navegador con el cual se realizara las pruebas puede ser Chrome, Firefox, Edge y Safari.
        Además de el modo Headless, que nos sirve para realizar las pruebas sin mostrar interfaz gráfica y asi
        optimizar los recursos; y también el modo Grid, que nos permite realizar multiples pruebas desde distintos
        entornos.
        :param navigator: str: Nombre del navegador por default Chrome.
        :return:
        """
        try:
            if navigator.lower() == "chrome":
                self.driver = Chrome().iniciar_chrome()
            elif navigator.lower() == "firefox":
                self.driver = Firefox().iniciar_firefox()
            elif navigator.lower() == "edge":
                self.driver = Edge().iniciar_edge()
            elif navigator.lower() == "safari":
                self.driver = webdriver.Safari()
            elif navigator.lower() == "headless":
                self.driver = Headless().iniciar_headless()
            self.vars = {}
            return self.driver
        except Exception as e:
            print(e)