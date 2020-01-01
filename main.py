import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('say something: ')
    try:
        audio = r.listen(source)
        print('here')
        voice_data = r.recognize_google(audio)
        
        print(voice_data)
    except:
        print('something is wrong')
