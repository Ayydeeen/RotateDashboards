from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import schedule
import time

def refresh_webpage():
    browser.refresh()
    if "login" in browser.current_url:
        Login()
    Present()

#Function to input login credentials 
def Login():
    username = "user@domain.com"
    password = "pass"
    
    username_input = browser.find_element(By.NAME, "username")
    username_input.send_keys(username)
    
    password_input = browser.find_element(By.NAME, "password")
    password_input.send_keys(password)
    
    login_button = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div[3]/div/div/div[1]/form/div[3]/button")
    login_button.click()

#Function to click buttons that present a rotating dashboard
def Present():
    tv_button = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[1]/div[4]")
    tv_button.click()
    
    rotate_button = browser.find_element(By.XPATH, "/html/body/div[5]/fullscreen-opts/div/div[2]")
    rotate_button.click()
    
    time.sleep(2)
    
    present_button = browser.find_element(By.XPATH, "//*[@id='dashboard-playlists-modal']/div[4]/button[2]")
    present_button.click()

#Initial Window Opening
browser = webdriver.Firefox()

#Open webpage
browser.get('https://brightguage.com/board')

#Check to see if redirected to login page
if "login" in browser.current_url:
    Login()

#Sleep and start initial presentation
time.sleep(10)
Present()

# Schedule the refresh_webpage function to run every day at 8 am
schedule.every().day.at("08:00").do(refresh_webpage)

while True:
    schedule.run_pending()
    time.sleep(1)
