from gtts import gTTS
import os
speakit = "For information in english, speak english.   Hindi me jaankaari ke liye, bolen Hindi"
tts = gTTS(text=speakit, lang='hi')
tts.save("lang.mp3")
os.system("lang.mp3")
