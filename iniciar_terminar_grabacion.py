import subprocess
import signal

process = None

def start_recording():
    global process
    command = "parec --format=s16le --rate=44100 --channels=2 --latency-msec=1 --device=$(pactl list | grep -A2 'Source #0' | grep 'Name: ' | cut -d' ' -f2) | ffmpeg -f s16le -ar 44100 -ac 2 -i - output.wav"
    process = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)

def stop_recording():
    global process
    if process is not None:
        os.killpg(os.getpgid(process.pid), signal.SIGTERM)
        process = None