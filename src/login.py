from time import sleep
from selenium.webdriver.common.keys import Keys
from pageObjects.elements import get_input_login
from pageObjects.elements import get_input_passwd

def login(driver, time_sleep):
    driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
    sleep(time_sleep)
    get_input_login(driver).send_keys("candidato@justa.com.vc")
    get_input_passwd(driver).send_keys("tamojusto" + Keys.ENTER)


