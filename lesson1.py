from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     y = calc(x)
#     input1 = browser.find_element(By.ID, "answer")
#     input1.send_keys(y)
#     checkbox = browser.find_element(By.ID, "robotCheckbox")
#     checkbox.click()
#     radiobutton = browser.find_element(By.ID, "robotsRule")
#     radiobutton.click()
#     button = browser.find_element(By.TAG_NAME, "button")
#     button.click()
#
# finally:
#     time.sleep(5)
#     browser.quit()



# # get_attribute возвращает текстовое значение аттрибута
#
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     people_radio = browser.find_element(By.ID, "peopleRule")
#     people_checked = people_radio.get_attribute("checked")
#     print("value of people radio: ", people_checked)
#     assert people_checked is not None, "People radio is not selected by default"
#     assert people_checked == "true", "People radio is not selected by default"
#     # Если атрибута нет, то метод get_attribute вернёт значение None. Применим метод get_attribute
#     # ко второму radiobutton, и убедимся, что атрибут отсутствует.
#     robots_radio = browser.find_element(By.ID, "robotsRule")
#     robots_checked = robots_radio.get_attribute("checked")
#     assert robots_checked is None
#
# finally:
#     time.sleep(5)
#     browser.quit()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    chest = browser.find_element(By.TAG_NAME, "img")
    x = int(chest.get_attribute("valuex"))
    answer = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(answer)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()
    submit = browser.find_element(By.TAG_NAME, "button")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()