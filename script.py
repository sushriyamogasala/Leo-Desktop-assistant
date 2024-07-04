import speech_recognition as sr
import os


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language='en-in')
            print(f"Your command is {query} ")
        except:
            return ""
        if "hey luci" in query or "hey Lucy" in query or "wake up" in query:
            os.startfile('start.py')
    return query.lower()


while True:
    listen()