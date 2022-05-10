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
    i = 0   
    for lineas in lineas:
        usuarios.append(lineas)
    return usuarios

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(ubicacionDriver, chrome_options=options)
    correos=readUsuarios()
    driver.set_window_position(1000,0)
    driver.maximize_window()
    time.sleep(1)
    driver.get('https://www.telepizza.es/account/login')
    time.sleep(5)
    driver.find_element(By.XPATH,'//*[@id="cookie-alert"]/div/div[2]/button').click()
    i = 0
    for correo in correos:
        recover = driver.find_element(By.XPATH,'//*[@id="login-with-email"]').click()        
        time.sleep(10)
        recover = driver.find_element(By.ID,'Email')
        recover.clear()
        recover.send_keys(correo)
        time.sleep(10)
        recover = driver.find_element(By.XPATH,'//*[@id="main-content"]/div/div/div/form/div[2]/div/button').click()
        time.sleep(10)
        break
    driver.close()