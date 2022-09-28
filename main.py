from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


#calling the selenium driver
chrome_drive_path = r"C:\Users\gorem\Downloads\chromedriver_win32\chromedriver.exe"
ser = Service(chrome_drive_path)

driver = webdriver.Chrome(service=ser)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

#Finding Elements within the website
cookie = driver.find_element(By.ID, "cookie")
store = driver.find_elements(By.CSS_SELECTOR, "#store div")


#These are the timeout and end times for the game
check = time.time() + 1
finish = 0




#This will get the cookie clicking
game_on = True
while game_on:
    cookie.click()
    if time.time() > check:
        store = driver.find_elements(By.CSS_SELECTOR, "#store div:not(.grayed)")
        store[-1].click()
        finish += 1
        if finish == 60*5:
            game_on = False
        check += 1

#Finally we'll figure out how well we did
cpm = driver.find_element(By.ID, "cps")
print(f"Your final cookies per second was: {cpm.text}")
