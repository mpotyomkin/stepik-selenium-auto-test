from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    
    answer = browser.find_element_by_css_selector('[name="firstname"]')
    answer.send_keys("Миша")    
    
    answer = browser.find_element_by_css_selector('[name="lastname"]')
    answer.send_keys("Михайлов")    
  
    answer = browser.find_element_by_css_selector('[name="email"]')
    answer.send_keys("a@b.c")    
  
    answer = browser.find_element_by_id('file')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           
    # добавляем к этому пути имя файла 
    answer.send_keys(file_path)   
    
    
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