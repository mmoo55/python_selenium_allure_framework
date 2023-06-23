from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from session.session import session


class Control:

    def __init__(self, type, locator):
        """
        Constructor de inicio de la clase Control.
        :param type: Tipo de selector que se ingresará, puede ser de tipo:
                    id, name, link text, css selector, partial link text, class name, xpath.
        :param locator: elemento a referenciar de la página web.
        :return:
        """
        self.type = type
        self.locator = locator
        self.control: WebElement = None
        self.driver = session.get_browser()

    def find(self):
        """
        Encuentra y obtiene el elemento
        :return:
        """
        self.control = self.driver.find_element(self.type, self.locator)

    def scroll(self):
        """
        Realiza el scroll de la ventana hasta donde este visible el elemento
        :return:
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", self.control)

    def mouse_actions(self):
        """
        Obtiene el elemento para utilizar las opciones del mouse
        :return: ActionChains
        """
        return ActionChains(self.driver)

    def click(self):
        """
        Permite realizar una acción de 'click' en un elemento de la página web.
        :return:
        """
        self.find()
        print("Damos click en el campo -> {} ".format(self.locator))
        self.control.click()

    def click_derecho(self):
        """
        Permite realizar una acción 'click derecho' a un elemento de la página.
        :return:
        """
        self.find()
        self.scroll()
        self.mouse_actions().context_click(self.control).perform()

    def doble_click(self):
        """
        Permite realizar una acción de 'doble click' a un elemento de la página web.
        :return:
        """
        self.find()
        self.scroll()
        self.mouse_actions().double_click(self.control).perform()

    def control_es_visible(self):
        """
        Permite verificar si un elemento de la pagina web esta visible.
        :return: Boolean, True si es visible o de lo contrario False
        """
        try:
            self.find()
            return self.control.is_displayed()
        except:
            return False

    def get_text(self):
        """
        Obtiene el texto de un elemento.
        :return: str
        """
        self.find()
        return self.control.text

    def get_attribute(self, type_atribute):
        """
        Obtiene el valor de un atributo de un elemento.
        :param type_valor: tipo de valor que sera captado por la funcion "get_attibute".
        :return: str
        Example:
        # self.control.get_attribute('value')
        """
        self.find()
        return self.control.get_attribute(type_atribute)

    def wait_control_is_not_in_the_page(self):
        """
        Permite realizar una espera durante un tiempo determinado.
        :return:
        """
        explicit_wait = WebDriverWait(self.driver, 10)
        explicit_wait.until(EC.visibility_of_element_located(self.control))

    def desplazar_mouse_a_elemento(self):
        """
        Permite desplazar el puntero del mouse a un elemento web.
        :return:
        """
        self.find()
        # self.scroll()
        print("Desplazamiento en el campo -> {} ".format(self.locator))
        self.mouse_actions().move_to_element(self.control).perform()

    def desplazar_mouse_a_elemento_click(self):
        """
        Permite desplazar el puntero del mouse a un elemento y realiza 'click'
        :return:
        """
        self.find()
        # self.scroll()
        print("Desplazamiento y click en el campo -> {} ".format(self.locator))
        self.mouse_actions().move_to_element(self.control).click().perform()

    def enviar_archivo(self, path: str):
        """
        Permite enviar un archivo.
        :param path: La ruta donde se encuentra el archivo que será enviado.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} la ruta del archivo -> {} ".format(self.control, path))
        self.control.send_keys(path)