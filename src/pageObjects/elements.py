from selenium.webdriver.common.by import By

# Página -> http://automationpractice.com/index.php?controller=authentication&back=my-account
def get_input_login(driver):
    return driver.find_element(By.NAME, "email")

def get_input_passwd(driver):
    return driver.find_element(By.NAME, "passwd")


# Página -> http://automationpractice.com/index.php?id_product=1&controller=product
def get_bt_add_card(driver):
    return driver.find_element(By.NAME, "Submit")


# Página -> http://automationpractice.com/index.php?controller=order


# Página -> http://automationpractice.com/index.php?controller=order&step=1


# Página -> http://automationpractice.com/index.php?controller=address&back=order.php%3Fstep%3D1&id_address=719519


# Página -> http://automationpractice.com/index.php?fc=module&module=cheque&controller=payment