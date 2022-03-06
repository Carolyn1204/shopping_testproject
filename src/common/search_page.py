from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from src.common.base import BaseClass


class SearchPage(BaseClass):
    url = "https://www.roots.com/ca/en/homepage"
    # page elements
    search_icon = (By.XPATH, "//*[@class='header-icon-search']")
    search_input = (By.ID, "searchInput")
    adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")
    num = 1

    # elements operations
    def search(self, search_content):
        # self.open_url(self.url)
        # self.maximize_window()
        # self.close_popup()

        self.clicks(self.search_icon, self.num)
        self.click(self.search_input)
        self.input(self.search_input, search_content)
        self.locator(self.search_input).send_keys(Keys.ENTER)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    sp = SearchPage(driver)
    sp.search("sweater")
