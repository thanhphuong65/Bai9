from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import time

chrome_driver_path = "C:\Chorme Driver\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://itmscoaching.herokuapp.com/form")

driver.find_element_by_id('first-name').send_keys("Binh")
driver.find_element_by_id('last-name').send_keys("Nguyen")
driver.find_element_by_id('job-title').send_keys("Tester")
driver.find_element_by_id('radio-button-3').click()
driver.find_element_by_id('checkbox-2').click()
Select(driver.find_element_by_id('select-menu')).select_by_value('3')
driver.find_element_by_id('datepicker').send_keys("20/7/2011")

time.sleep(2)
# driver.find_element_by_class_name('register').click()

driver.find_element_by_xpath(
    '/html/body/div/form/div/div[8]/a').click()


time.sleep(5)
driver.quit()
