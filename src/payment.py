from selenium.webdriver.common.by import By
from time import sleep

def payment(driver, time_sleep):
    submit_checkbox = driver.find_element(By.NAME, "cgv")
    submit_checkbox.click()
    sleep(time_sleep)

    bt_proceed = driver.find_element(By.NAME, "processCarrier")
    bt_proceed.click()

    driver.get("http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment")
