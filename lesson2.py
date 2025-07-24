from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math, time

# # Работа со списками
# try:
#     link = 'http://suninjuly.github.io/selects2.html'
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num1 = int(browser.find_element(By.ID, 'num1').text)
#     num2 = int(browser.find_element(By.ID, 'num2').text)
#     res = num1 + num2
#     select = Select(browser.find_element(By.ID, "dropdown"))
#     select.select_by_value(str(res))
#     submit = browser.find_element(By.TAG_NAME, "button")
#     submit.click()
#
# finally:
#     time.sleep(5)
#     browser.quit()


# # JS скрипты

# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# try:
#     # browser = webdriver.Chrome()
#     # browser.execute_script("document.title='Script executing';alert('Robots at work');")
#
#     # ошибка с перекрытым элементом(не кликнуть)
#     browser = webdriver.Chrome()
#     link = "https://suninjuly.github.io/execute_script.html"
#     browser.get(link)
#     x = int(browser.find_element(By.ID, "input_value").text)
#     res = calc(x)
#     input1 = browser.find_element(By.ID, 'answer')
#     input1.send_keys(res)
#     robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
#     robot_checkbox.click()
#     robots_rule = browser.find_element(By.ID, "robotsRule")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", robots_rule)
#     robots_rule.click()
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
#
# finally:
#     time.sleep(5)
#     browser.quit()


# Загрузка файлов
import os

# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)                                # отправляем файл


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    first_name = browser.find_element(By.CSS_SELECTOR, "input[name=firstname]")
    first_name.send_keys('Ivan')
    last_name = browser.find_element(By.CSS_SELECTOR, 'input[name=lastname]')
    last_name.send_keys('Ivanov')
    email= browser.find_element(By.CSS_SELECTOR, 'input[name=email]')
    email.send_keys('test@test.ru')
    file = browser.find_element(By.ID, "file")
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(file_path, 'file.txt')
    file.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()