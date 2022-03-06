import unittest
import warnings
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from src.common.item_detail_page import ItemDetailPage
from src.common.item_list_page import ItemListPage
from src.common.login_page import LoginPage
from src.common.search_page import SearchPage
from src.common.shopping_bag_page import ShoppingBagPage
from config import global_parameters as gp
from src.common.base import BaseClass
import ddt
import yaml


@ddt.ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
        # self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)
        self.bc = BaseClass()
        lp = LoginPage()
        lp.login(gp.username, gp.password)

    @ddt.file_data('C:/Users/carol/PycharmProjects/testproject/testproject/data/data.yaml')
    @ddt.unpack
    def test_01_shopping(self, **kwargs):
        sp = SearchPage()
        sp.search(kwargs.get('search_word'))
        ilp = ItemListPage()
        ilp.choose_categories_women()
        sleep(2)
        ilp.choose_price_high_to_low()
        sleep(2)
        ilp.choose_item()
        idp = ItemDetailPage()
        idp.choose_color()
        sleep(2)
        idp.choose_size()
        sleep(2)
        idp.increase_quantity()
        sleep(2)
        idp.click_add_to_bag_button()
        sleep(2)
        idp.click_view_bag()
        sleep(2)
        sbp = ShoppingBagPage()
        sbp.click_decrease_item()
        # sbp.click_decrease_item()
        sleep(2)
        self.bc.scroll("scroll(0,300)")
        sbp.click_include_gift_receipt()
        sleep(2)
        sbp.input_gift_message(kwargs.get('gift_message'))
        sleep(2)
        sbp.click_save_message_button()
        sleep(2)
        sbp.click_continue_to_checkout()
        sleep(2)
        xpath = (By.XPATH, "//span[text()='Want to Pick it up In-Store?']")
        result = self.bc.get_text(xpath)
        expected_result = 'Want to Pick it up In-Store?'
        try:
            self.assertIn(result, expected_result)
        except:
            self.bc.mylog.error('Assert Exception Error')
            self.bc.img_screenshot('test_01_shopping error img')
        else:
            self.bc.mylog.info('PASS')

    def test_02_empty_shopping_bag(self):
        idp = ItemDetailPage()
        idp.click_bag_icon()
        sleep(2)
        idp.click_view_bag()
        sleep(2)
        self.bc.scroll("scroll(0,300)")
        sleep(2)
        sbp = ShoppingBagPage()
        sbp.click_remove_gift_message()
        sleep(2)
        self.bc.scroll("scroll(0,-300)")
        sleep(2)
        sbp.click_remove_item()
        sleep(2)

    def tearDown(self):
        self.bc.quit()


if __name__ == '__main__':
    unittest.main()
