import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# try:
#     link = 'http://suninjuly.github.io/cats.html'
#     browser = webdriver.Chrome()
#     browser.get(link)
#     browser.find_element(By.ID, "button")
#
# finally:
#     browser.quit()


# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")

# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    book = browser.find_element(By.ID, 'book')
    price = WebDriverWait(browser, 12).until(
           EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    book.click()
    x = browser.find_element(By.ID, "input_value").text
    res = calc(int(x))
    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(res)
    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit.click()


finally:
    time.sleep(10)
    browser.quit()
