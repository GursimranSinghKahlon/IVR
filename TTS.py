from gtts import gTTS
import os
speakit = "Hello"
tts = gTTS(text=speakit, lang='hi')
tts.save("lang.mp3")
os.system("lang.mp3")
