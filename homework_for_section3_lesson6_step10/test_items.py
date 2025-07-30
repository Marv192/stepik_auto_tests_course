import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket_button(browser):
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket'), "No add button"
    time.sleep(20)

