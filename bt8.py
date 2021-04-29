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

driver.find_element_by_id('username').send_keys("tomsmith")

elem = driver.find_element_by_id('password')
elem.send_keys("SuperSecretPassword!")

time.sleep(2)
# driver.find_element_by_class_name('register').click()

driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div/div/div/div/div[1]/div/div[1]/form/p[3]/input[3]').click()

print(driver.title)

time.sleep(5)
driver.quit()
