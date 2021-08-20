import pyaudio
import time
import threading
import numpy
import audioop
import sys
AUDIO_DATA=None
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 4096
audio = pyaudio.PyAudio()
recodrding_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
def audio_playing():
    playing_stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)
    while(True):
        if AUDIO_DATA!=None:
            playing_stream.write(AUDIO_DATA)
threading.Thread(target=audio_playing,daemon=True).start()
while(True):
    DATA=recodrding_stream.read(CHUNK)
    AUDIO_DATA=audioop.mul(DATA,2,0.1)
    print(sys.getsizeof(AUDIO_DATA)/1024)
recodrding_stream.close()