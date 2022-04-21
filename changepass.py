import string, random, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from ctypes import sizeof
ubicacionDriver = '/usr/local/bin/chromedriver'

def readUsuarios():
    usuarios = list()
    arc = open("user.txt")
    lineas = arc.readlines()
    i = 0    #driver.get('https://www.abcdin.cl/')
    for lineas in lineas:
        usuarios.append(lineas)
    return usuarios

def readPasswords():
    passwords = list()
    arc = open("pass.txt")
    lineas = arc.readlines()
    i = 0
    for lineas in lineas:
        passwords.append(lineas)
    return passwords


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(ubicacionDriver, chrome_options=options)
    correo = ['diego.carrillo.1331@gmail.com']
    passnew=['newPASS123']
    passold=['oldPASS123'] # pass recien cambiada
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)
    driver.get('https://www.abcdin.cl/customer/account/login/')
    time.sleep(5)
    email = driver.find_element(By.ID, "email")
    email.clear()
    email.send_keys(correo)
    time.sleep(1)
    passw = driver.find_element(By.ID,"pass")
    passw.clear()
    passw.send_keys(passold)
    time.sleep(1)
    driver.find_element(By.ID, "send2").click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="maincontent"]/div[2]/div[1]/div[4]/div[2]/div/div[2]/a[2]/span').click()
    time.sleep(5)
    
    contant = driver.find_element(By.ID,'current-password')
    contant.clear()
    contant.send_keys(passold)
    time.sleep(2)

    new = driver.find_element(By.ID,'password')
    new.clear()
    new.send_keys(passnew)
    time.sleep(2)

    new = driver.find_element(By.ID,'password-confirmation')
    new.clear()
    new.send_keys(passnew)
    time.sleep(2)

    driver.find_element(By.XPATH,'//*[@id="form-validate"]/div[2]/div[1]/button').click()
    time.sleep(200)
    driver.close()