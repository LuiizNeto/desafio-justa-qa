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

def edit(driver, time_sleep, first_exec=False):
    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)
    driver.get("http://automationpractice.com/index.php?controller=address&id_address=723017")
    sleep(time_sleep)

    address = "Rua Itaberaba"
    address_number = "90"
    city = "Recife"
    state = "Hawaii"
    postal_code = "00090"
    home_phone = "34420922"
    phone = "81991485511"
    information = "Informação adicional para teste."
    email = "luiznelson150@outlook.com"

    if first_exec != False:
        address = "Av Brasil"
        address_number = "23"
        city = "Brasilia"
        state = "Alaska"
        postal_code = "00053"
        home_phone = "32680593"
        phone = "81985838286"
        information = "Desafio para Q.A Justa."
        email = "luiznelson140@gmail.com"
        
    input_address = get_input_address(driver)
    input_address.clear()
    input_address.send_keys(address)

    input_address_number = get_input_address_number(driver)
    input_address_number.clear()
    input_address_number.send_keys(address_number)

    input_city = get_input_city(driver)
    input_city.clear()
    input_city.send_keys(city)

    input_state = get_input_state(driver)
    for option in input_state:
        if option.text == state:
            option.click()
            break

    input_postal_code = get_input_postal_code(driver)
    input_postal_code.clear()
    input_postal_code.send_keys(postal_code)

    input_home_phone = get_input_home_phone(driver)
    input_home_phone.clear()
    input_home_phone.send_keys(home_phone)

    input_phone = get_input_phone(driver)
    input_phone.clear()
    input_phone.send_keys(phone)

    input_information = get_input_information(driver)
    input_information.clear()
    input_information.send_keys(information)

    input_email = get_input_email(driver)
    input_email.clear()
    input_email.send_keys(email)

    bt_save= get_bt_save(driver)
    bt_save.click()

    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)
    
    bt_process = get_bt_process_address(driver)
    bt_process.click()
    sleep(time_sleep)