from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    chest = browser.find_element_by_id('treasure')
    x = chest.get_attribute('valuex')
    y = calc(x)
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    robotCheckbox.click()
    rules = browser.find_element_by_id('robotsRule') 
    rules.click()
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()