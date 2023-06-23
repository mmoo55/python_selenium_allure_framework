import re

import os
from config import basedir

from selenium.webdriver.common.by import By

from control.label import Label


class FuncionesExtra:

    def get_tipo_valor(self, clave_valor):
        """Obtiene el tipo de valor.

        :param clave_valor: descripcion del valor creado.
        :Usage:
            ::

                clave_valor = "VTD-TD-NA"
                clave_valor_split = clave_valor.split("-")
                calve_valor_str = clave_valor_split[0]
                calve_valor_str = "VTD"

        :rtype: str
        """
        print(f"LA CLAVE PASADA ES LA SIGUIENTE {clave_valor}")
        clave_valor_split = clave_valor.split("-")
        calve_valor_str = clave_valor_split[0]
        print(f"EL CODIGO ES {calve_valor_str}")
        return calve_valor_str

    def get_successful_code(self, mensaje_exitoso):
        """Obtiene el codigo de del mensaje exitoso de un registro.

        :param mensaje_exitoso: mensaje de registro exitoso.
        :Usage:
            ::

                mensaje_exitoso = "Registro exitoso con codigo BOVTDAAA0001"
                code_raw = mensaje_exitoso.split(" ")
                code_clean = code_raw[len(code_raw) - 1]
                calve_valor_str = "BOVTDAAA0001"

        :rtype: str
        """
        code_raw = mensaje_exitoso.split(" ")
        code = code_raw[len(code_raw) - 1]
        code_clean = re.sub(r'[^a-zA-Z0-9]', '', code)
        return code_clean

    def get_table_head_position(self, thead: str, title: str):
        """Obtiene la posicion de una columna.

        :param thead: parte del localizador de la parte superior de la tabla.
        :param title: el encabezado de la columna a buscar.

        :rtype: int
        """
        column_number = 1
        thead_label = Label(By.XPATH, thead+f"//th[{column_number}]//span")

        while thead_label.get_text() != title:
            column_number += 1
            thead_locator = thead + f"//th[{column_number}]//span"
            thead_label = Label(By.XPATH, thead_locator)

        return column_number

    def get_status_column_number(self, thead, title):
        """Obtiene la posicion de la columna "Estado" a partir de la posicion de cierta columna pasada como parametro.

        :param driver: instancia del navegador actual que se esta utilizando.
        :param thead: parte del localizador de la parte superior de la tabla.
        :param title: el encabezado de la columna a buscar, la cual será el punto de partida para buscar la columna "Estado".

        :rtype: int
        """
        estado_title_column_number = self.get_table_head_position(thead, "Estado")
        codigo_emision_column_number = self.get_table_head_position(thead, title)

        estado_column_number = estado_title_column_number - codigo_emision_column_number

        return estado_column_number

    def obtener_ruta_archivo(self, file_name: str):
        """
        Permite obtener la ruta de un archivo.
        :param file_name: Nombre del archivo con extensión.
        :return: str
        """
        for r, d, f in os.walk(basedir):
            for file in f:
                if file == file_name:
                    ruta = os.path.abspath(os.path.join(r, file))
                    print(ruta)
                    return ruta