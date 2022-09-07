from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    number_1 = browser.find_element(By.ID, "num1")
    num1 = int(number_1.text)
    number_2 = browser.find_element(By.ID, "num2")
    num2 = int(number_2.text)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(num1+num2))


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    browser.quit()
