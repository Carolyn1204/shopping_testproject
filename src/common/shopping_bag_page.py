from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from src.common.search_page import BaseClass


class ShoppingBagPage(BaseClass):
    increase_item = (By.XPATH, "//span[@class='qty-icon plus']")
    decrease_item = (By.XPATH, "//span[@class='qty-icon minus']")
    edit_item = (By.XPATH, "//span[@class='edit']")
    remove_item = (By.XPATH, "//span[@class='remove']")
    add_to_wishlist = (By.XPATH, "//span[@class='move-to-wishlist']")
    include_gift_receipt = (By.XPATH, "//button[@id='sendgift']//span[@class='root-plus']")
    gift_message = (By.XPATH, "//textarea[@class='input-textarea ']")
    save_message_button = (By.XPATH, "//button[@id='savegiftdetails']")
    continue_to_checkout = (By.XPATH, "//a[contains(@class,'button-text')]")
    remove_gift_message = (By.XPATH, "//a[@id='removeGiftOptions']")

    def click_increase_item(self):
        self.click(self.increase_item)

    def click_decrease_item(self):
        self.click(self.decrease_item)

    def click_edit_item(self):
        self.click(self.edit_item)

    def click_add_to_wishlist(self):
        self.click(self.add_to_wishlist)

    def click_include_gift_receipt(self):
        self.click(self.include_gift_receipt)

    def input_gift_message(self, gift_message):
        self.input(self.gift_message, gift_message)

    def click_save_message_button(self):
        self.click(self.save_message_button)

    def click_continue_to_checkout(self):
        self.click(self.continue_to_checkout)

    def click_remove_gift_message(self):
        self.click(self.remove_gift_message)

    def click_remove_item(self):
        self.click(self.remove_item)
        # item_lists = self.driver.find_elements("//span[@class='remove']")
        # for item in item_lists:
        #     item.click()
        #     sleep(2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    sbp = ShoppingBagPage(driver)
    sbp.click_increase_item()
    sleep(2)
    sbp.click_decrease_item()
    sbp.click_include_gift_receipt()
    sbp.input_gift_message()
    sbp.click_continue_to_checkout()
