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
    correo=['ljimenez@gorecoquimbo.cl']
    contraseña =['A202cb962ac5912%']

    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)
    driver.get('https://www.telepizza.es/account/login')
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="cookie-alert"]/div/div[2]/button').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="main-content"]/div/div/div[2]/div/a').click()
    time.sleep(5)

    scorreo = driver.find_element(By.XPATH,'//*[@id="RegisterUserName"]')
    scorreo.clear()
    scorreo.send_keys(correo)
    time.sleep(5)

    passw = driver.find_element(By.XPATH,'//*[@id="RegisterPassword"]')
    passw.clear()
    passw.send_keys(contraseña)
    time.sleep(1)
    
    passw = driver.find_element(By.XPATH,'//*[@id="RegisterConfirmPassword"]')
    passw.clear()
    passw.send_keys(contraseña)
    time.sleep(1)
    
    driver.find_element(By.XPATH,'//*[@id="ActivityTypesViewModel_CustomerActivitiesViewModel_1__Value"]').click()
    time.sleep(10)
    
    driver.find_element(By.XPATH,'//*[@id="register-form-content"]/div[7]/div/input').click()
    time.sleep(20)
    driver.close()