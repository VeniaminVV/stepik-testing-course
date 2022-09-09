from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_elem1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        input_elem1.send_keys("lol1")
        input_elem2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        input_elem2.send_keys("lol2")
        input_elem3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        input_elem3.send_keys("lol3")
                

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Smth gone wrong!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input_elem1 = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
        input_elem1.send_keys("lol1")
        input_elem2 = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
        input_elem2.send_keys("lol2")
        input_elem3 = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
        input_elem3.send_keys("lol3")
                

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Smth gone wrong!")

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(2)
        # закрываем браузер после всех манипуляций
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()