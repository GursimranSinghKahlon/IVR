import speech_recognition as sr
from gtts import gTTS
import os
import time
import subprocess
import threading
r = sr.Recognizer()
t=0

def windowsmedia(filename):
    os.system(filename)
def startmp3(filename,timex):
    mythread = threading.Thread(target=windowsmedia,args=[filename])
    mythread.start()
    time.sleep(timex) #You might want to extend this... I just give it 15 seconds to complete before killing the process.
    os.system('taskkill /f /im wmplayer.exe')

    
with sr.Microphone() as source:
    while(t==0):
        t=1
        startmp3('lang.mp3',8)
        print ('Say Something!')
        audio = r.listen(source,timeout=2000)
        print ('Done!')
        try:
            text = r.recognize_google(audio)
            print('You said: '+text)
            if(text=='English' or text=='english' or text=='angrezi' or text=='Angrezi' or text=='angregi' or text=='Angregi' or text=='angreji' or text=='Angreji' ):
                startmp3('eng.mp3',10)
                print ('Say Something!')
                audio = r.listen(source,timeout=2000)
                print ('Done!')
                try:
                    text = r.recognize_google(audio)
                    print('You said: '+text)
                    os.system("mere.mp3")                    
                except:
                    pass
                    os.system("thanks_en.mp3")

            elif(text=='Hindi' or text=='hindi'):
                startmp3('hindi.mp3',5)
                print ('Say Something!')
                audio = r.listen(source,timeout=2000)
                print ('Done!')
                try:
                    text = r.recognize_google(audio)
                    print('You said: '+text)
                    os.system("mere.mp3")                    
                except:
                    pass
                    os.system("thanks_en.mp3")                    
            else:
                print('Try Again')
                startmp3('tryagain_hi.mp3',4)
                pass
                
        except:
            t=0
            print('Try Again')
            startmp3('tryagain_hi.mp3',4)
            pass
        
