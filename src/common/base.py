import datetime
import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from config import global_parameters as gp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from util import logger


class BaseClass(object):
    def __init__(self, driver):
        self.driver = driver
        self.mylog = logger.LogUtil()


    @staticmethod
    def current_date():
        dt = datetime.datetime.now()
        return dt.strftime("%Y-%m-%d")

    # visit url
    def open_url(self, url):
        try:
            self.driver.get(url)
            self.mylog.info("open url:" + str(url))
        except:
            self.mylog.error('cannot open the webpage')

    # locate element
    def locator(self, loc):
        try:
            return self.driver.find_element(*loc)
        except:
            self.mylog.error('cannot find the element')

    # locate elements
    def locators(self, loc):
        try:
            return self.driver.find_elements(*loc)
        except:
            self.mylog.error('cannot find the elements')

    def get_text(self, loc):
        try:
            text = self.driver.find_element(*loc).text
            self.mylog.info('get text: ' + text)
            return text
        except:
            self.mylog.error('cannot get the text')

    # click
    def click(self, loc):
        # WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(loc), message='the element is unvisible')
        try:
            self.locator(loc).click()
            self.mylog.info("click the element:" + str(loc))
        except:
            self.mylog.error('the element is unclickable' + str(loc))

    def clicks(self, loc, num):
        try:
            self.locators(loc)[num].click()
        except:
            self.mylog.error('the elements is unclickable')

    # maximize window
    def maximize_window(self):
        self.driver.maximize_window()
        self.mylog.info("maxmize the window")

    # implicitly wait
    def implicitly_wait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # input
    def input(self, loc, txt):
        #  WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc), message='cannot find the elements')
        try:
            self.locator(loc).send_keys(txt)
            self.mylog.info("input the text" + str(txt))
        except:
            self.mylog.error('misinput')

    def scroll(self, scroll_range):
        self.driver.execute_script(scroll_range)

    # quit
    def quit(self):
        self.driver.quit()
        self.mylog.info("quit the driver")

    # close
    def close(self):
        self.driver.close()
        self.mylog.info("close the driver")

    # if popup exists
    def close_popup(self):
        if self.driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-closethick']"):
            popup_value = (By.XPATH, "//span[@class='ui-icon ui-icon-closethick']")
        try:
            self.click(popup_value)
            self.mylog.info("close the popup")
        except:
            self.mylog.error('cannot close the popup')

    def img_screenshot(self, img_name):
        dt = datetime.datetime.now()
        try:
            self.driver.get_screenshot_as_file(gp.img_path + img_name + '_' + BaseClass.current_date() + '.png')
        except:
            self.mylog.error('fail to take a screenshot:' + img_name + '.png')

    # def my_assert(self, result, expected_result, img_name):
    #     try:
    #         self.assertIn(result, expected_result)
    #     except NoSuchElementException as e:
    #         self.img_screenshot(img_name)
    #     except AssertionError as e:
    #         print('Results do not match Expectations')
    #     except Exception as e:
    #          print('Unknown Error')
    #     else:
    #         self.mylog.info('PASS')

    # def popup(self, loc):
    #     flag = True
    #     try:
    #         self.click(*loc)
    #         return flag
    #     except:
    #         flag = False
    #         return flag

if __name__ == '__main__':
    b = BaseClass()
