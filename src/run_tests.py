from selenium import webdriver
from add_products import add
from edit_address import edit
from payment import payment
from login import login

driver = webdriver.Chrome()
time_sleep = 2

# Caso de teste 1
def test_1():
    login(driver, time_sleep)
    add(driver, time_sleep)
    edit(driver, time_sleep)
    payment(driver, time_sleep)


# Caso de teste 2
def test_2():
    login(driver, time_sleep)
    add(driver, time_sleep)
    edit(driver, time_sleep)
    payment(driver, time_sleep)


# Caso de teste 3
def test_3():
    login(driver, time_sleep)
    add(driver, time_sleep, True)
    payment(driver, time_sleep)


test_3()