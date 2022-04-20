import string, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ctypes import sizeof
ubicacionDriver = '/usr/local/bin/chromedriver'


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(ubicacionDriver, chrome_options=options)
    correo=['mgallardor@gorecoquimbo.cl']
    contraseña =['6c0eb35162d3e5a06a096d67589cfa97']

    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)
    driver.get('https://www.abcdin.cl/customer/account/create/')
    time.sleep(5)
    nombre = driver.find_element(By.ID,"firstname")
    nombre.clear()
    nombre.send_keys('random')
    time.sleep(1)
    
    apellido = driver.find_element(By.ID,"lastname")
    apellido.clear()
    apellido.send_keys('random')
    time.sleep(1)

    rut = driver.find_element(By.ID,"rut")
    rut.clear()
    rut.send_keys('11111111-1')
    time.sleep(1)

    dia = driver.find_element(By.ID,"dob-day")
    dia.clear()
    dia.send_keys('12')
    time.sleep(1)

    mes = driver.find_element(By.ID,"dob-month")
    mes.clear()
    mes.send_keys('12')
    time.sleep(1)

    mes = driver.find_element(By.ID,"dob-year")
    mes.clear()
    mes.send_keys('2000')
    time.sleep(1)

    driver.find_element(By.ID,"gender").click()
    driver.find_element(By.XPATH,'//*[@id="gender"]/option[3]').click()
    time.sleep(1)

    tel = driver.find_element(By.ID,"customer_telephone")
    tel.clear()
    tel.send_keys('912345678')
    time.sleep(1)

    mail = driver.find_element(By.ID,"email_address")
    mail.clear()
    mail.send_keys(correo)
    time.sleep(1)

    password = driver.find_element(By.ID,"password")
    password.clear()
    password.send_keys(contraseña)
    time.sleep(1)

    passwordconfirmation = driver.find_element(By.ID,"password-confirmation")
    passwordconfirmation.clear()
    passwordconfirmation.send_keys(contraseña)
    time.sleep(1)

    driver.find_element(By.ID,"is_subscribed").click()
    driver.find_element(By.ID,"term_conditions").click()
    time.sleep(10)
    driver.find_element(By.ID,"recaptcha-checkbox-border").click()
    time.sleep(10)


    driver.close()