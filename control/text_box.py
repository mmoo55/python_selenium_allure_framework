from control.control import Control
from selenium.webdriver.common.keys import Keys

class TextBox(Control):

    def __init__(self, type, locator):
        super(TextBox, self).__init__(type, locator)

    def set_text(self, texto: str):
        """
        Permite escribir el texto de entrada en un elemento de tipo INPUT/ Caja de texto.
        :param texto: Texto alfanumérico que se ingresara a la caja de texto.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.send_keys(texto)

    def set_text_clear(self, texto: str):
        """
        Limpia la caja de texto y permite escribir el texto de entrada en un elemento de tipo INPUT/ Caja de texto.
        :param texto: Texto alfanumérico que se ingresara a la caja de texto.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.clear()
        self.control.send_keys(texto)

    def clear_textbox(self):
        """
        Limpia la caja de texto.
        :return:
        """
        self.find()
        print("Limpiando el campo {}".format(self.control))
        self.control.clear()

    def set_text_tab(self, texto: str):
        """
        Permite escribir el texto de entrada en un elemento de tipo INPUT/ Caja de texto y realizar una tabulación.
        :param texto: Texto alfanumérico que se ingresara a la caja de texto.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.send_keys(texto)
        self.control.send_keys(Keys.TAB)

    def set_text_enter(self, texto: str):
        """
        Permite escribir el texto de entrada en un elemento de tipo INPUT/ Caja de texto y realizar un ENTER.
        :param texto: Texto alfanumérico que se ingresara a la caja de texto.
        :return:
        """
        self.find()
        print("Escribiendo en el campo {} el texto -> {} ".format(self.control, texto))
        self.control.send_keys(texto)
        self.control.send_keys(Keys.ENTER)