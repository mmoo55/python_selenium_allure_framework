from Control.Select import SelectFunction
from control.button import Button
from control.label import Label

import time
from enum import Enum

# from Session.Session import session


class FuncionesDate:

    def datepicker_a(self, fecha: str):
        """
        Permite seleccionar una fecha en un campo/elemento de tipo Datepicker.
        :param fecha: Fecha en formato dd/mm/yyyy
        :return:
        """
        day, month, year = self.formato_fecha(fecha)
        month = month[0:3]

        # Year
        SelectFunction("xpath", "//select[@class='ui-datepicker-year']").seleccionar_por_texto_visible(year)
        # Month
        SelectFunction("xpath", "//select[@class='ui-datepicker-month']").seleccionar_por_texto_visible(month)
        # Day
        xpath_day = "//a[text()='{}']".format(day)

        Button("xpath", xpath_day).click()

    def datepicker_b(self, fecha: str):
        """
        Permite seleccionar una fecha en un campo/elemento de tipo Date picker.
        :param fecha: Fecha en formato dd/mm/yyyy
        :return:
        """
        label_month = Label("xpath", "//span[@class='ui-datepicker-month']")
        label_year = Label("xpath", "//span[@class='ui-datepicker-year']")
        button_back_month = Button("xpath", "//span[@class='ui-icon ui-icon-circle-triangle-w']")
        button_next_month = Button("xpath", "//span[@class='ui-icon ui-icon-circle-triangle-e']")

        day, month, year = self.formato_fecha(fecha)
        if int(label_year.get_text()) == int(year):
            pass
        elif int(year) > int(label_year.get_text()):
            while year != label_year.get_text():
                button_next_month.click()
            if label_month.get_text() != month:
                while month != label_month.get_text():
                    button_next_month.click()
        else:
            while year != label_year.get_text():
                button_back_month.click()
            if label_month.get_text() != month:
                while month != label_month.get_text():
                    button_back_month.click()

        xpath_day = "//a[text()='{}']".format(day)
        time.sleep(1)
        Button("xpath", xpath_day).click()

    def formato_fecha(self, fecha: str):
        """
        Permite formatear la fecha.
        :param fecha: Fecha de entrada en formato dd/mm/yyyy
        :return: day, month, year
        """
        month_names = Enum("Months", [("Enero", 1), ("Febrero", 2), ("Marzo", 3), ("Abril", 4), ("Mayo", 5),
                                      ("Junio", 6), ("Julio", 7), ("Agosto", 8), ("Septiembre", 9),
                                      ("Octubre", 10), ("Noviembre", 11), ("Diciembre", 12)])

        array_fecha = []
        if "/" in fecha:
            array_fecha = fecha.split("/")
        elif "-" in fecha:
            array_fecha = fecha.split("-")

        day = int(array_fecha[0])
        month = int(array_fecha[1])
        year = array_fecha[2]

        return day, month_names(month).name, year