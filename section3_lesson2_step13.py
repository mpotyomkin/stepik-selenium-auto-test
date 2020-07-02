from selenium import webdriver
import time
import unittest


class MyTest(unittest.TestCase):

    def test_page2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first = browser.find_element_by_xpath('//input[contains(@class, "first") and @required]')
        first.send_keys("Ivan")
        second = browser.find_element_by_xpath('//input[contains(@class, "second") and @required]')
        second.send_keys("Ivanov")
        third = browser.find_element_by_xpath('//input[contains(@class, "third") and @required]')
        third.send_keys("a@b.c")


        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text, 
            "successful registraion expected."
        )
        browser.quit()
        

    def test_page1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first = browser.find_element_by_xpath('//input[contains(@class, "first") and @required]')
        first.send_keys("Ivan")
        second = browser.find_element_by_xpath('//input[contains(@class, "second") and @required]')
        second.send_keys("Ivanov")
        third = browser.find_element_by_xpath('//input[contains(@class, "third") and @required]')
        third.send_keys("a@b.c")


        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(
            "Congratulations! You have successfully registered!", welcome_text, 
            "successful registraion expected."
        )
        browser.quit()
        
if __name__ == "__main__":
    unittest.main()
