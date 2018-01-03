import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    while(1):
        print ('Say Something!')
        audio = r.listen(source,timeout=4000)
        print ('Done!')
        try:
            text = r.recognize_google(audio)
            print('req text: '+text)
        except:
            pass
        

