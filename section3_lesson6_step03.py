import time
import math

def calc():
    return str(math.log(int(time.time())))
    
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

# '.smart-hints__hint' '<textarea' '#ember78'  '.submit-submission'
# textarea string-quiz__textarea ember-text-area ember-view
# textarea string-quiz__textarea ember-text-area ember-view
@pytest.mark.parametrize('url', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])

def test_allien(browser, url):
# from selenium.webdriver.common.by import By

    browser.get(url)

    time.sleep(5)
    
    answer_el = browser.find_element_by_css_selector(
        '.textarea.string-quiz__textarea.ember-text-area.ember-view'
    )
    answer_el.send_keys( calc() )

    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()
    
    
    class="stepik-fonts-loaded ember-application"
    
    time.sleep(30)
    
    The owls are not what they seem! OvO

