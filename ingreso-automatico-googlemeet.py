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
import subprocess
import signal
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

process = None

def start_recording():
    global process
    command = "parec --format=s16le --rate=44100 --channels=2 --latency-msec=1 --device=$(pactl list | grep -A2 'Source #5' | grep 'Name: ' | cut -d' ' -f2) | ffmpeg -f s16le -ar 44100 -ac 2 -i - AHORASIDAILY.wav"
    process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)

def stop_recording():
    global process
    if process is not None:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process = None

class meet_bot:
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=/home/juan/pepe2")  # Path to your chrome profile
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        self.bot =  webdriver.Chrome(executable_path="/home/juan/Downloads/chromedriver", options=options)



    def join(self, meeting_link):
        bot = self.bot
        bot.get(meeting_link)
        wait = WebDriverWait(bot, 2)
        try:
          join_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button")))
          join_btn.click()
          print("Se hizo clic en el primer boton")
    
# Si no se encuentra el primer boton, intentar con el segundo boton
        except:
          join_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button")))
          join_btn.click()
          print("Se hizo clic en el segundo boton")
        start_recording()
        input()
        stop_recording()
        

obj = meet_bot()
obj.join('https://meet.google.com/byv-fmct-nfn')

