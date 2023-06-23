from control.text_box import TextBox


class SelectExtra(TextBox):

    def __init__(self, type, locator):
        super(SelectExtra, self).__init__(type, locator)

    def     select_item(self, text_item: str):
        """
        Permite realizar click al elemento/componente de tipo select y buscar en sus options.
        :param text_item: texto de entrada para la busqueda
        :return:
        """
        if text_item != "":
            self.click()
            locator_main = self.locator
            if "label" in self.locator:
                locator_aux = self.locator[0:len(self.locator)-6]
            else:
                locator_aux = self.locator
            self.locator = locator_aux + "_filter"
            self.set_text_enter(text_item)
            self.locator = locator_main