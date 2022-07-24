from selenium.webdriver.common.by import By
from time import sleep
from pageObjects.elements import get_submit_checkbox, get_bt_proceed, get_bt_confirm

def payment(driver, time_sleep):
    get_submit_checkbox(driver).click()
    get_bt_proceed(driver).click()
    driver.get("http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment")
    sleep(time_sleep)
    bt = get_bt_confirm(driver)
    bt.click()
