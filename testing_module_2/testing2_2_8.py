import os 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    link = " http://suninjuly.github.io/file_input.html"
    browser.get(link)

    name_input = browser.find_element(By.NAME, "firstname")
    name_input.send_keys("Stewen")
    surname_input = browser.find_element(By.NAME, "lastname")
    surname_input.send_keys("Lolovich")
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("slolovich@gmail.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_element = browser.find_element(By.NAME, "file")    
    file_path = os.path.join(current_dir, 'file.txt')
    file_element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
                
    

finally:
    time.sleep(10)
    browser.quit()
    