from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = "C:\Chorme Driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://practice.automationtesting.in/")

driver.find_element_by_id('menu-item-50').click()

driver.find_element_by_id('reg_email').send_keys("balabauaamxen@gmail.com")

elem = driver.find_element_by_id('reg_password')
elem.send_keys("21312sadjas123")

time.sleep(5)
driver.find_element_by_class_name('register').click()

driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[2]/form/p[3]/input[3]').click()
