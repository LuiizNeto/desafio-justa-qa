from selenium.webdriver.common.by import By
from time import sleep
from pageObjects.elements import get_input_address
from pageObjects.elements import get_input_address_number
from pageObjects.elements import get_input_city
from pageObjects.elements import get_input_state
from pageObjects.elements import get_input_postal_code
from pageObjects.elements import get_input_home_phone
from pageObjects.elements import get_input_phone
from pageObjects.elements import get_input_information
from pageObjects.elements import get_input_email
from pageObjects.elements import get_bt_save
from pageObjects.elements import get_bt_process_address

def edit(driver, time_sleep):
    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)
    driver.get("http://automationpractice.com/index.php?controller=address&id_address=723017")
    sleep(time_sleep)
    get_input_address(driver).clear().send_keys("Rua Itaberaba")
    get_input_address_number(driver).clear().send_keys("70")
    get_input_city(driver).clear().send_keys("Salvador")

    for option in get_input_state(driver):
        if option.text == "Florida":
            option.click()
            break

    input_postal_code = get_input_postal_code(driver)
    input_postal_code.clear()
    input_postal_code.send_keys("00016")
    sleep(time_sleep)

    input_home_phone = get_input_home_phone(driver)
    input_home_phone.clear()
    input_home_phone.send_keys("34426014")
    sleep(time_sleep)

    input_phone = get_input_phone(driver)
    input_phone.clear()
    input_phone.send_keys("81991485511")
    sleep(time_sleep)

    get_input_information(driver).clear().send_keys("Desafio Justa!")
    sleep(time_sleep)

    get_input_email(driver).clear().send_keys("luiznelson150@outlook.com")
    sleep(time_sleep)

    get_bt_save(driver).click()
    sleep(time_sleep)

    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)
    
    get_bt_process_address(driver).click()
    sleep(time_sleep)