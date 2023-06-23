from selenium import webdriver

from browser.IBrowser import IBrowser


class Grid(IBrowser):

    def create(self):
        # self.driver = webdriver.Chrome(executable_path=r"C:\drivers selenium\chromedriver_win32\chromedriver.exe")
        #
        # self.driver.implicitly_wait(30)
        # self.driver.set_page_load_timeout(30)
        # self.driver.maximize_window()
        #
        # return self.driver
        pass