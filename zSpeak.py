import pyglet
pyglet.lib.load_library('avbin64')
pyglet.have_avbin64=True
import time
from gtts import gTTS

def speak(t):
    tts = gTTS(text=t, lang='en')
    filename = 'tts.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    time.sleep(music.duration)