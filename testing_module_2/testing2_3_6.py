from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    trollface_button = browser.find_element(By.CLASS_NAME, "trollface")
    trollface_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = math.log(abs(12*math.sin(x)))

    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(str(result))

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()