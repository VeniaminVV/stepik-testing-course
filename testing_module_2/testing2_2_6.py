import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try :
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = math.log(abs(12*math.sin(x)))
    browser.execute_script("window.scrollBy(0, 100);")

    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(str(result))

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(10)
    browser.quit()