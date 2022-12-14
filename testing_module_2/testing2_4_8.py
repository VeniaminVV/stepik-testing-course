from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    price_100 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")    
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    result = math.log(abs(12*math.sin(x)))

    input_element = browser.find_element(By.ID, "answer")
    input_element.send_keys(str(result))

    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
    