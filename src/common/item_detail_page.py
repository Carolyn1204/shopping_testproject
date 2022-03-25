from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.common.base import BaseClass


class ItemDetailPage(BaseClass):
    # url = "https://www.roots.com/ca/en/fair-isle-sweater-stein-38070157.html?selectedColor=004&cgid=Womens&start=2&q" \
    #      "=sweater&itemsourse=productlist "
    # page elements
    item_color = (By.XPATH, "//a[contains(text(),'NOMAD MIX')]")
    item_size = (By.XPATH, "//a[@title='Large']/span[text()='L']")
    add_quantity = (By.XPATH, "//div[@class='qty-block-increase']/span[@class='increase-qty unselectable']")
    add_to_bag = (By.XPATH, "//button[@id='add-to-cart']")
    bag_icon = (By.XPATH, "//div[@id='cartTotal']")
    num = 1
    view_bag = (By.XPATH, "//a[contains(@class,'mini-cart-link-cart')]")
    #adver_close = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")

    # elements operations
    def choose_color(self):
        #self.open_url(self.url)
        #self.maximize_window()
        #sleep(2)
        #self.close_popup(self.adver_close)
        #sleep(2)
        self.click(self.item_color)

    def choose_size(self):
        self.click(self.item_size)

    def increase_quantity(self):
        self.click(self.add_quantity)

    def click_add_to_bag_button(self):
        self.click(self.add_to_bag)

    def click_bag_icon(self):
        self.clicks(self.bag_icon, self.num)

    def click_view_bag(self):
        self.click(self.view_bag)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    idp = ItemDetailPage(driver)
    idp.choose_color()
    idp.choose_size()
    idp.increase_quantity()
    idp.click_add_to_bag_button()
    sleep(2)
    idp.click_view_bag()
