from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
try:
    #Открыть страницу http://suninjuly.github.io/explicit_wait2.html
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    
    #Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    #Нажать на кнопку "Book"
    button = browser.find_element_by_xpath('//button[text()="Book"]')
    button.click()

    #Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    input1 = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.send_keys(y)
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(25)
    # закрываем браузер после всех манипуляций
    browser.quit()