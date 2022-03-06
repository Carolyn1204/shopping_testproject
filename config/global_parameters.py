import os
from datetime import time
from selenium import webdriver

'''project_path'''
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

'''log path'''
log_path = project_path+"\\log\\"

'''exception images path'''
img_path = project_path + "\\img\\"

'''report path'''
report_path = project_path + "\\report\\"

'''testcase path'''
testcase_path = project_path + "\\src\\test_cases\\"


'''browser'''
driver = webdriver.Chrome()

'''login parameters'''
url = "https://www.roots.com/on/demandware.store/Sites-RootsCA-Site/en_CA/Account-Show"
username = "1659145340@qq.com"
password = "1204fighting"

'''Email parameters'''
receiver_address = '421761464@qq.com'
sender_address = '1659145340@qq.com'
sender_password = 'tkguiuxgskkwbcgj'


