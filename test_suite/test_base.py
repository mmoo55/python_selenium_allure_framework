import unittest

from util.get_env import load_env
from session.session import session
from util.funciones_extra import FuncionesExtra

# Ingresar al Home
from page.login_page import LoginPage

# Main page
from page.main_page import MainPage

###### ALLURE ######
import allure
import pytest

class TestBase(unittest.TestCase):
    # Login
    login_section = LoginPage()

    main_section = MainPage()

    # # MENUS
    # menu_cuentas = CuentasMenu()
    # menu_emisiones = EmisionesMenu()

    # FUNCIONES EXTRA
    funcion_extra = FuncionesExtra()

    # Obteniendo los datos base
    USERNAME = load_env.get_username()
    PASSWORD = load_env.get_password()

    def setUp(self):
        # Configurando Navegador
        session.get_browser().get(load_env.get_url())

        # Login
        # self.login_section.ingresar_login(self.USERNAME, self.PASSWORD)

        session.get_instance().get_browser().implicitly_wait(5)

    def tearDown(self):
        session.get_instance().close_session()