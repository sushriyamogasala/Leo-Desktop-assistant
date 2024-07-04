import datetime
import speech_recognition as sr 
from time import *
import webbrowser as web
from pytube import *
from pyautogui import *
import wikipedia
import os 
from RPS import rps
import random
import pyttsx3
import pyautogui
import screen_brightness_control as sb
import psutil
import cv2
import pywhatkit
from keyboard import press_and_release
import requests
import pyjokes
#import randfacts
#from tkinter import *
import subprocess
import pyperclip
import psutil
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
#import geocoder
# import speedtest
import pyaudio
import winsound
# import speedtest
# import Face_recognition

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    print(f"{audio}") 
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        #print(f"User said: {query}")
        speak("user said: "+ query)
    except Exception as e:
        speak("Say that again please...")
        return "None"
    return query.lower()

MASTER = " Team "

def wishme():
    press('esc')
    speak("User Authentication Successful")
    hour = int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good morning "+ MASTER)
    elif 12<=hour<16:
        speak("Good afternoon " + MASTER)
    else:
        speak("Good evening "+ MASTER)

    speak("I am Leo, please tell me how may i help you")
    
def execute():
    #print(9)
    while True:
        query = takecommand().lower()
        
        if "hello" in query or "hi" in query or "hey" in query:
            speak("hi team ")

        elif "how are you" in query:
            speak("i'm fine team thank u . What about u?")

        elif "not fine" in query:
            speak('why team what happened ?')

        elif "i am fine" in query or 'fine' in query :
            speak("Glad to hear that team")

        elif "what are you doing" in query:
            speak("I am preparing myself for u team")

        elif 'who are you' in query:
            speak("Hello! I'm Leo, your virtual personal assistant here to make your life a bit easier.")
        
        elif 'what can you do' in query:
            speak("I'm equipped to assist you with a variety of tasks, from setting reminders and answering questions to providing information and helping you stay organized. Feel free to let me know how I can assist you today!")
        
        elif "do you love me " in query:
            speak("Yes team , ofcourse i love u to the moon and back")
        
        elif "what time is it" in query or "what is the time" in query:
            p = strftime("%H")
            r = strftime("%M")
            speak("Current time is " + p + " hours " + r + " minutes")

        elif "what day is it" in query:
            now = datetime.datetime.today().strftime("%A")
            speak("Today is " + now)

        elif "what is today's date" in query or "what's today's date" in query:
            g = datetime.datetime.today().strftime("%d")
            e = datetime.datetime.today().strftime("%m")
            t = datetime.datetime.today().strftime("%Y")
            speak("Today's date is " + g + " " + e + " " + t)

        elif "which month we are in" in query:
            e = datetime.datetime.today().strftime("%m")
            speak(f"{e}")

        elif "which year is this" in query:
            t = datetime.datetime.today().strftime("%Y")
            speak(f"{t}")

        elif "wikipedia" in query:


            speak('Searching in wikipedia')
            query = query.replace('wikipedia'," ")
            results = wikipedia.summary(query,sentences=2)
            speak("According the information on wikipedia")
            #print(results)
            speak(results)
            

            
        elif ('play music' in query) or ('music' in query):
            
            
            speak("yes mam it's time for some music , i'm also bored working all this time ")
            speak('Here are your favorites')
            
            music_dir = 'C:\\Users\\sushr\\Music\\Ammayi.mp3'

            try:
                songs = os.startfile(music_dir)

                '''if len(songs) > 0:
                    n = random.randint(0, len(songs) - 1)
                    os.startfile(os.path.join(music_dir, songs[n]))
                    sleep(30)
                else:
                    print("No songs found in the music directory.")'''

            except Exception as e:
                print(f"An error occurred: {e}")
                        
        elif 'open youtube' in query:
            speak("we are about to launch into youtube")
            web.open("youtube.com")

        elif 'open linkedin' in query:
            speak('entering your linkedin community')
            web.open('linkedin.com')

        elif 'open github' in query:
            speak('let"s dive into Github world')
            web.open('github.com\sushriyamogasala')

        elif 'open data file' in query:
            speak('opening your file')
            file = r"D:\Projects\DataSets-master.zip\DataSets-master"
            os.startfile(file)
        #elif 'open '
        
        elif 'start game' in query:
            speak("Launching rock paper scissors game on the console.......Dont cheat ")
            rps()

        elif "volume" in query:
            vol(query)

        elif "brightness" in query:
            brightness(query)

        elif "battery" in query:
            battery()

        elif "current location" in query:
            cl()

        elif "capture photo" in query or "picture" in query:
            photo()

        elif "shutdown" in query:
            shut()

        elif "restart" in query:
            res()

        elif "capture video" in query:
            video()

        elif "search on youtube" in query:
            query = query.replace("search", "")
            query = query.replace("on youtube", "")
            speak(f"Searching {query} on youtube")
            youtube(query)

        

        elif "chrome mode" in query or 'chrome mod' in query:
            chromemode()

        # elif "test speed" in query:
        #     speedTest(query)

        # elif "remember this" or "note" in query:
        #     remember(query)

        elif "remind me" in query:
            rem()

        elif "youtube mode" in query or 'youtube mod' in query:
            yta()

        elif "download this video" in query:
            speak("Your video is being downloaded team...")
            ytd()

        elif "google search" in query:
            query = query.replace("google search", "")
            google(query)

        elif "whatsapp" in query:
            whatsapp()

        elif "instagram" in query:
            insta()

        elif "news" in query:
            news()

        elif 'joke' in query:
            jokes()

        elif 'fact' in query:
            facts()

        elif 'take screenshot' in query:
            screenshot()

        elif "take rest" in query or 'leo sleep' in query or 'quit' in query or 'logout' in query or 'log out' in query:
            speak("Ok team , setting sleep mode")
            speak("If you need any help, just say hey leo")
            exit()

        else:
            speak("Unable to get that team, will work on it")

def vol(query):
    if "volume up" in query:
        pyautogui.press("volumeup")
        speak("Your volume is increased")

    elif "volume down" in query:
        pyautogui.press("volumedown")
        speak("Your volume is decreased")

    elif "mute volume" in query:
        pyautogui.press("volumemute")
        speak("Your volume is muted")

def brightness(query):
    if "increase brightness" in query:
        sb.set_brightness(100)
        speak("Your brightness is set to high")

    elif "decrease brightness" in query:
        sb.set_brightness('-100')
        speak("Your brightness is set to low")

    elif "medium brightness" in query:
        sb.set_brightness(50)
        speak("Your brightness is set to medium")


def battery():
    battery = psutil.sensors_battery()
    speak(f"Your battery percent is {battery.percent}")

    if battery.power_plugged:
        speak("Your PC is plugged in")

    else:
        speak("Your PC is unplugged")

    convert(battery.secsleft)

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    speak(f"Your pc will function upto {hour} hour {minutes} minutes")

def cl():
    r=requests.get('https://get.geojs.io./')
    ipreq=requests.get('https://get.geojs.io/v1/ip.json')
    ipadd=ipreq.json()['ip']

    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
    georeq=requests.get(url)
    geodata=georeq.json()

    speak(f"Latitude : {geodata['latitude']}")
    speak(f"Longitude : {geodata['longitude']}")
    speak(f"City : {geodata['city']}")
    speak(f"Region : {geodata['region']}")
    speak(f"Country : {geodata['country']}")
    speak(f"Timezone : {geodata['timezone']}")

def photo():
    speak("say cheese")
    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    for i in range(3):
        sleep(1)
        return_value, image = camera.read()
        cv2.imwrite('D:\Projects\Suzie desktop assistant\photos\opencv' + str(i) + '.png', image)
    del camera


def video():  #==================================================================================================================================================================================
    speak("Get ready , the video will start in a second")
    vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    vid_cod = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("D:\Projects\Suzie desktop assistant\videos\cam_video.mp4v", vid_cod, 20.0, (640, 480))
    #speak("press, 'g', to stop your video")
    start_time = time.time()
    while True:
        ret, frame = vid_capture.read()
        cv2.imshow("My cam video", frame)
        output.write(frame)

        if time.time() - start_time >= 10:
            break

        if cv2.waitKey(1) & 0XFF == ord('g'):
            break

    vid_capture.release()
    output.release()
    cv2.destroyAllWindows()


def shut():
    speak("Your System will shutdown in 5 seconds")
    os.system("shutdown /s /t 5")


def res():
    speak("Your System will restart in 5 seconds")
    os.system("shutdown /r /t 5")

def google(query):
    speak(f"Searching {query} on google")
    pywhatkit.search(query)

def youtube(query):
    result = "https://www.youtube.com/results?search_query=" + query
    web.open(result)
    speak("This is what i found for your search .")
    pywhatkit.playonyt(query)
    speak("This may also help you.")


def chromemode():
    speak("Chrome mode activated")
    web.open(url='https://www.google.com')
    speak("Tell your command team")
    while True:
        try:
            com = takecommand()
            print(com)
            com = com.lower()
            if "incognito tab" in com:
                press_and_release('ctrl + shift + n')
            elif "new tab" in com:
                press_and_release('ctrl + t')
            elif "new window" in com:
                press_and_release('ctrl + n')
            elif "switch tab" in com:
                press_and_release('ctrl + tab')
            elif "downloads" in com or 'download' in com:
                press_and_release('ctrl + j')
            elif "history" in com:
                press_and_release('ctrl + h')
            elif "close tab" in com:
                press_and_release('ctrl + w')
            elif "reopen closed tab" in com:
                press_and_release('ctrl + shift + t')
            elif "reload" in com:
                press_and_release('ctrl + r')
            elif "back" in com:
                press_and_release('alt + left')
            elif "next" in com:
                press_and_release('alt + right')
            elif "close window" in com:
                press_and_release('alt + f4')
            elif "bookmark" in com:
                press_and_release('ctrl + shift + o')
            elif "clear browsing data" in com:
                press_and_release('ctrl + shift + delete')
            elif "search" in com:
                speak("what to search ?")
                com = takecommand()
                google(com)
            elif "source code" in com:
                press_and_release('ctrl + u')
            elif "add to bookmark" in com:
                press_and_release('ctrl + d')
            elif "scroll down" in com:
                press_and_release('space')
            elif "scroll up" in com:
                press_and_release('shift + space')
            elif "exit chrome mode" in com:
                pyautogui.hotkey('ctrl', 'w')
                speak("Chrome mode exited")
                break
        except:
            continue

# def speedTest(query):
#     speak("Checking Your internet speed....")
#     speed = speedtest.Speedtest()
#     downloading = speed.download()
#     cd = int(downloading / 800000)
#     uploading = speed.upload()
#     cu = int(uploading / 800000)
#     if 'uploading' in query:
#         speak(f"Uploading speed is {cu} mbps")
#     elif 'downloading' in query:
#         speak(f"Downloading speed is {cd} mbps")
#     else:
#         speak(f"Uploading speed is {cu} mbps and Downloading speed is {cd} mbps") 


# def remember(rmsg):
#     rmsg = rmsg.replace("remember this", "")
#     rmsg = rmsg.replace("leo ", "")
#     remember = open('notes/remember.txt', 'w+')
#     remember.write(rmsg)
#     remember.close()
#     speak("ok, i remember this. ask me to remind you whenever you want .")
    
def rem():
    
    speak("You told me to remind you this message")
    process = subprocess.Popen(['python', 'DesktopNotifier.py'])
    time.sleep(5)
    process.terminate()


def yta():
    speak("Youtube mode activated")
    web.open(url='https://www.youtube.com/')
    speak("Tell your command team")
    while True:
        try:
            com = takecommand()
            print(com)
            com = com.lower()
            if "pause" in com:
                press_and_release('space bar')
            elif "play" in com:
                press_and_release('space bar')
            elif "full screen" in com:
                press_and_release('f')
            elif "exit full screen" in com:
                press_and_release('esc')
            elif "theatre mode" in com:
                press_and_release('t')
            elif "fast forward" in com:
                press_and_release('l')
            elif "back forward" in com:
                press_and_release('j')
            elif "increase speed" in com:
                press('>')
            elif "decrease speed" in com:
                press('<')
            elif "reload" in com:
                press_and_release('ctrl + r')
            elif "previous" in com:
                press_and_release('shift + p')
            elif "next" in com:
                press_and_release('shift + n')
            elif "close youtube" in com:
                press_and_release('alt + f4')
            elif "download this" in com:
                ytd()
            elif "history" in com:
                web.open("https://www.youtube.com/feed/history")
            elif "search" in com:
                speak("what do you want to search for ?")
                query = takecommand()
                result = "https://www.youtube.com/results?search_query=" + query
                web.open(result)
                speak("This is what i found for your search .")
                speak("This may help you.")
            elif "open youtube" in com:
                web.open(url='https://www.youtube.com/')
            elif "exit youtube mode" in com or "exit youtube mod" in query:
                pyautogui.hotkey('ctrl', 'w')
                break

        except:
            continue

def ytd():
    sleep(5)
    try:
        click(x=942, y=59)
        # click(x=1250, y=75)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'c')
        link = pyperclip.paste()
        Link = str(link)
        YouTube(Link).streams.first().download('videos\\')
        speak("Your video has been downloaded and saved to videos folder")
    except:
        return ""
    
def insta():
    web.open('https://www.instagram.com')


def news():
    apikey = "4ad432c899d345f6b946ed73db668cbd"
    mainurl = "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4ad432c899d345f6b946ed73db668cbd"
    news = requests.get(mainurl).json()
    article = news['articles']
    newsarticle = []
    for arti in article:
        newsarticle.append(arti['title'])

    for i in range(5):
        speak(newsarticle[i])
        engine.runAndWait()


def jokes():
    speak(pyjokes.get_joke())


def facts():
    speak(randfacts.get_fact())

def screenshot():
    # try:
        myScreenshot = pyautogui.screenshot()
        x = str(datetime.datetime.now())
        myScreenshot.save('photos/ss_'+x+'.png')
        speak("screenshot is taken and saved to photos in Lucy folder .")
    # except:
    #     pass

# def security():
#     speak("Recognizing and Verifying face...Please wait...")

#     if Face_recognition.facerec():
#         wishme()
#         execute()

#     else:
#         speak("Face recognition failed")
#         speak("Enter correct password to get access")
#         try:
#             def check():
#                 if pwd.get() == "riya":
#                     speak("Access granted!")
#                     win.destroy()
#                     wishme()
#                     execute()
#                 else:
#                     speak("Incorrect password... Terminating Program...")
#                     win.destroy()
#                     exit()

#             win = Tk()
#             win.title('Verification')
#             win.geometry("800x400")
#             win.config(background="black")
#             pwd = StringVar()
#             msg = Label(text="Enter Password :", font=('Comic Sans MS', 16, "bold"), background="black", fg='White')
#             msg.place(x=100, y=100)
#             entry = Entry(win, textvariable=pwd, font=15, bd='3')
#             entry.place(x=400, y=110)
#             set = Button(text="Submit", command=check, font=('Comic Sans MS', 13), bg='#567', fg='White')
#             set.place(x=330, y=200)
#             win.mainloop()

#         except:
#             print()

if __name__=="__main__":
    speak("hello team")
    wishme()
    execute()
    #takecommand()
    

    


