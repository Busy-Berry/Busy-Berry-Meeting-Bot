import subprocess
import signal
import os
import hashlib
import boto3
import datetime
import time
from flask import Flask, render_template, request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

process = None

def start_recording():
    global process
    command = "parec --format=s16le --rate=44100 --channels=2 --latency-msec=1 --device=$(pactl list | grep -A2 'Source #0' | grep 'Name: ' | cut -d' ' -f2) | ffmpeg -f s16le -ar 44100 -ac 2 -i - audio.wav"
    process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)

def stop_recording():
    
    global process
    if process is not None:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process = None

class MeetBot:
    def __init__(self):
        options = Options()
        options.add_argument("user-data-dir=/home/ubuntu/nuevamente/subir/pepe2/")  # Path to your chrome profile
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        self.bot = webdriver.Chrome(executable_path="/home/ubuntu/nuevamente/subir/chromedriver", options=options)

    def join(self, meeting_link):
        bot = self.bot
        bot.get(meeting_link)
        wait = WebDriverWait(bot, 5)
        try:
            join_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[13]/div[3]/div/div[1]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button")))
            join_btn.click()
            print("Se hizo clic en el primer botón")

        # Si no se encuentra el primer botón, intentar con el segundo botón
        except:
            join_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button")))
            join_btn.click()
            print("Se hizo clic en el segundo botón")
        start_recording()
        while True:
            time.sleep(1)
        stop_recording()
        bot.save_screenshot('viscreenshotantesdemorir.png')
        with open('viantesdepaginalogin.html', 'w') as f:
            f.write(html)
        
    def stopperer(self):
        bot = self.bot
        wait = WebDriverWait(bot, 5)
        stop_recording()
        html = bot.page_source
        bot.save_screenshot('screenshot.png')
        with open('paginalogin.html', 'w') as f:
            f.write(html)
# Nombre del archivo de audio
        audio_file = "audio.wav"
# Ruta completa del archivo de audio
        audio_file_path = os.path.join(os.getcwd(), audio_file)

# Obtener la fecha actual
        current_date = datetime.datetime.now()
# Convertir la fecha en formato de cadena
        current_date_str = current_date.strftime("%Y-%m-%d")
# Generar el hash MD5 de la fecha
        md5_hash = hashlib.md5(current_date_str.encode()).hexdigest()
# Nombre de la carpeta con el hash MD5 y la fecha
        folder_name = md5_hash + "_" + current_date_str
# Configurar cliente de AWS S3
        s3_client = boto3.client('s3',aws_access_key_id='AKIAZVXONNLLTFMZQJDT',aws_secret_access_key='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',region_name='us-east-1')
# Enviar archivo a S3 dentro de la carpeta
        bucket_name = 'busy-berry-meet-records'
        s3_key = folder_name + "/" + audio_file
        s3_client.upload_file(audio_file_path, bucket_name, s3_key)
        
        file_path = "audio.wav"

        if os.path.exists(file_path):
            os.remove(file_path)
            print("El archivo audio.wav ha sido eliminado.")
        else:
            print("El archivo audio.wav no existe.")

        

app = Flask(__name__)
bot = MeetBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/join-meeting', methods=['POST'])
def join_meeting():
    meeting_link = request.form.get('meeting_link')
    if meeting_link:
        bot.join(meeting_link)
        return 'Bot joined meeting successfully.'
    else:
        return 'Invalid meeting link.'

@app.route('/stop-recording', methods=['POST'])
def stop_recording_route():
    bot.stopperer()
    return 'Recording stopped successfully.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6550)
