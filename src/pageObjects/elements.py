from selenium.webdriver.common.by import By

# Página -> http://automationpractice.com/index.php?controller=authentication&back=my-account
def get_input_login(driver):
    return driver.find_element(By.NAME, "email")

def get_input_passwd(driver):
    return driver.find_element(By.NAME, "passwd")


# Página -> http://automationpractice.com/index.php?id_product=1&controller=product
def get_bt_add_card(driver):
    return driver.find_element(By.NAME, "Submit")

def get_input_address(driver):
    return driver.find_element(By.NAME, "address1")

def get_input_address_number(driver):
    return driver.find_element(By.NAME, "address2")

def get_input_city(driver):
    return driver.find_element(By.NAME, "city")

def get_input_state(driver):
    return driver.find_element(By.NAME, "id_state")

def get_input_postal_code(driver):
    return driver.find_element(By.NAME, "postcode")

def get_input_home_phone(driver):
    return driver.find_element(By.NAME, "phone")

def get_input_phone(driver):
    return driver.find_element(By.NAME, "phone_mobile")

def get_input_information(driver):
    return driver.find_element(By.NAME, "other") 

def get_input_email(driver):
    return driver.find_element(By.NAME, "alias")

def get_bt_save(driver):
    return driver.find_element(By.NAME, "submitAddress")

def get_bt_process_address(driver): 
    return driver.find_element(By.NAME, "processAddress")

def get_submit_checkbox(driver):
    return driver.find_element(By.NAME, "cgv")

def get_bt_proceed(driver):
    return driver.find_element(By.NAME, "processCarrier")

def get_bt_process_address(driver):
    return driver.find_element(By.NAME, "processAddress")