from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.common.base import BaseClass


class ItemListPage(BaseClass):
    #url = "https://www.roots.com/on/demandware.store/Sites-RootsCA-Site/en_CA/Search-Show?q=sweater"
    # page elements
    categories = (
        By.XPATH, "//div[contains(@class,'desktopRefinements')]//div[contains(@class,'categoryrefinement')]/h3/span")
    categories_women = (By.XPATH, "//ul[@id='category-level-1']//a[@class='refinement-link ']")
    num = 0
    personalized = (By.XPATH, "//span[text()='Personalized']")
    price_high_to_low = (By.XPATH, "//div[@class='selectric-scroll']//li[@data-index='4']")
    num2 = 1
    first_item = (By.XPATH, "//a[@class='thumb-link ']/picture/img")
    num3 = 1
    #adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")

    # elements operations
    def choose_categories_women(self):
        #self.open_url(self.url)
        #self.maximize_window()
        #sleep(3)
        #self.close_popup(self.adver_close)
        self.click(self.categories)
        self.clicks(self.categories_women, self.num)

    def choose_price_high_to_low(self):
        self.click(self.personalized)
        self.clicks(self.price_high_to_low, self.num2)

    def choose_item(self):
        self.clicks(self.first_item, self.num3)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    il = ItemListPage(driver)
    il.choose_categories_women()
    sleep(3)
    il.choose_price_high_to_low()
    sleep(3)
    il.choose_item()
