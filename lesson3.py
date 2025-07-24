from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# try:
#     link = 'http://suninjuly.github.io/alert_accept.html'
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.CSS_SELECTOR, '.btn')
#     button.click()
#     alert = browser.switch_to.alert
#     alert.accept()
#     x = browser.find_element(By.ID, "input_value").text
#     print(x, type(x))
#     print('hi')
#     res = calc(int(x))
#     input_answer = browser.find_element(By.ID, "answer")
#     input_answer.send_keys(res)
#     submit = browser.find_element(By.TAG_NAME, 'button')
#     submit.click()
# finally:
#     time.sleep(10)
#     browser.quit()


try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element(By.ID, "input_value").text
    res = calc(int(x))
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(res)
    submit = browser.find_element(By.TAG_NAME, 'button')
    submit.click()
finally:
    time.sleep(10)
    browser.quit()
