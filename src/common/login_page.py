from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.common.base import BaseClass
from config import global_parameters as gp


class LoginPage(BaseClass):

    # page elements
    email = (By.ID, "dwfrm_login_username")
    pwd = (By.ID, "dwfrm_login_password")
    rememberMe = (By.ID, "lbl_dwfrm_login_rememberme")
    signIn_button = (By.ID, "login")
    createNow_button = (By.ID, "create-an-account-now-button")
    track_order = (By.CLASS_NAME, "trackright")
    adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")

    # elements operations

    # def get_url(self):
    #     self.open_url(gp.url)

    def login(self, email_v, pwd_v):
     #   self.close_popup()
     #   sleep(2)
        self.input(self.email, email_v)
        self.input(self.pwd, pwd_v)
        sleep(1)
        self.click(self.rememberMe)
        sleep(1)
        self.click(self.signIn_button)

    def create_account(self):
        self.click(self.createNow_button)

    def track_order(self):
        self.click(self.track_order)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    email_value = 'abc'
    pwd_value = '12312345'

    lp = LoginPage(driver)
    lp.login(email_value, pwd_value)
