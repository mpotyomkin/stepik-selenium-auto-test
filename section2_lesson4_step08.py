from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    message = browser.find_element_by_id("price")
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    
    book = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
    book.click()


    time.sleep(1)

    submit = browser.find_element_by_css_selector('[type="submit"]')
    browser.execute_script(
        "return arguments[0].scrollIntoView(true);",     
        submit
    )
    submit.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    
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