from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import datetime
import time
import os
import keyboard
from selenium.webdriver.common.by import By
#https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#:~:text=The%20default%20location%20is%20in,Google%5CChrome%20Beta%5CUser%20Data

class meet_bot:
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=/home/juan/pepe")  # Path to your chrome profile
#        options.add_argument('--headless')
#        options.add_argument('window-size=1920x1080')
        self.bot =  webdriver.Chrome(executable_path="/home/juan/Downloads/chromedriver", options=options)

#    def login(self, email, pas):
#        bot = self.bot
#        bot.get(
#            "https://meet.google.com/enw-vsnc-uqe")
#        time.sleep(20)
#        email_in = bot.find_element(
#            By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
#        email_in.send_keys(email)
#        next_btn = bot.find_element(
#            By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button")
#        next_btn.click()
#        time.sleep(10)
#        pas_in = bot.find_element(
#            By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
#        pas_in.send_keys(pas)
#        next1_btn = bot.find_element(
#            By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]")
#        next1_btn.click()
#        time.sleep(2)

    def join(self, meeting_link):
        bot = self.bot
        bot.get(meeting_link)
        time.sleep(50)
        mute_btn = bot.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[5]/div[1]")
        mute_btn.click()
        blind_btn = bot.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[1]/div[1]/div/div[5]/div[2]")
        blind_btn.click()
        time.sleep(50)
        callate_btn = bot.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/div[2]/button")
        callate_btn.click()
        join_btn = bot.find_element(By.XPATH,"/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[2]/div/div[2]/div[1]/div[1]")
        join_btn.click()
        time.sleep(100)

obj = meet_bot()
obj.join('https://meet.google.com/miv-ybsz-oea')