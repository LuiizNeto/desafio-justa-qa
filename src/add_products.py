from time import sleep
from selenium.webdriver.common.by import By
from pageObjects.elements import get_bt_add_card, get_bt_process_address

def add(driver, time_sleep, is_test_3=False):
    driver.get("http://automationpractice.com/index.php?id_product=1&controller=product")
    sleep(time_sleep)
    get_bt_add_card(driver).click()
    sleep(time_sleep)
    driver.get("http://automationpractice.com/index.php?controller=order")
    sleep(time_sleep)

    if is_test_3:
        driver.get("http://automationpractice.com/index.php?controller=order&step=1")
        sleep(time_sleep)    
        get_bt_process_address(driver).click()
        sleep(time_sleep)
        return

    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)