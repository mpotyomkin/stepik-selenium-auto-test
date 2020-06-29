from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    submit = browser.find_element_by_css_selector('[type="submit"]')
    submit.click()

    time.sleep(1)
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)
    
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