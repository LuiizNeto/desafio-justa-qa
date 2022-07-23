from selenium.webdriver.common.by import By
from time import sleep

def edit(driver, time_sleep):
    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)
    driver.get("http://automationpractice.com/index.php?controller=address&id_address=723017")
    sleep(time_sleep)
    input_address = driver.find_element(By.NAME, "address1")
    input_address.clear()
    input_address.send_keys("Rua Itaberaba")

    input_address2 = driver.find_element(By.NAME, "address2")
    input_address2.clear()
    input_address2.send_keys("70")

    input_city = driver.find_element(By.NAME, "city")
    input_city.clear()
    input_city.send_keys("Salvador")

    input_state = driver.find_element(By.NAME, "id_state")
    for option in input_state.find_elements(By.TAG_NAME, "option"):
        if option.text == "Florida":
            option.click() 
            break

    input_postal_code = driver.find_element(By.NAME, "postcode")
    input_postal_code.clear()
    input_postal_code.send_keys("00016")
    sleep(time_sleep)

    input_home_phone = driver.find_element(By.NAME, "phone")
    input_home_phone.clear()
    input_home_phone.send_keys("34426014")
    sleep(time_sleep)

    input_phone = driver.find_element(By.NAME, "phone_mobile")
    input_phone.clear()
    input_phone.send_keys("81991485511")
    sleep(time_sleep)

    input_information = driver.find_element(By.NAME, "other")
    input_information.clear()
    input_information.send_keys("Desafio Justa!")
    sleep(time_sleep)

    input_email = driver.find_element(By.NAME, "alias")
    input_email.clear()
    input_email.send_keys("luiznelson150@outlook.com")
    sleep(time_sleep)

    bt_save = driver.find_element(By.NAME, "submitAddress")
    bt_save.click()
    sleep(time_sleep)

    driver.get("http://automationpractice.com/index.php?controller=order&step=1")
    sleep(time_sleep)
    
    bt_process_address = driver.find_element(By.NAME, "processAddress")
    bt_process_address.click()
    sleep(time_sleep)