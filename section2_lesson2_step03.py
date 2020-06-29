from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1el = browser.find_element_by_id('num1')
    x = num1el.text
    num2el = browser.find_element_by_id('num2')
    y = num2el.text
    result = str(int(x) + int(y))
    
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(result)
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()
    

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()