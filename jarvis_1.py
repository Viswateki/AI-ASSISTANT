from __future__ import with_statement
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests
import subprocess
from email.message import EmailMessage
import smtplib
# from decouple import config

# Initialize the pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

# Function to speak out the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time of the day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("ready to rock. What can I do for you?")

# Function to listen to user commands using speech recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

# To send emails we need to have permission from the google by creating an account on google cloud..@having an subscription incloud

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

# Getting the weather API key 
    
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
    

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def play_on_youtube(video):
    kit.playonyt(video)

# Main program starts here
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        
        
        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        # Search on YouTube
        elif 'search on youtube' in query:
            query = query.replace("search on youtube", "")
            webbrowser.open(f"https://www.google.com/={query}")
        
        # Open YouTube and play a specific video
        elif 'open youtube' in query:
            speak("What would you like to watch?")
            qrry = takeCommand().lower()
            kit.playonyt(f"{qrry}")
        
        # Close Chrome browser
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close msedge' in query:
            os.system("taskkill /f /im msedge.exe")
        
        # Close YouTube
        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'close youtube2' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close youtube3' in query:
            os.system("taskkill /f /im brave.exe")

        # Open Google and search
        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            webbrowser.open(f"{qry}")
            results = wikipedia.summary(qry, sentences=2)
            speak(results)

        # Close Google
        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")

        elif 'close google' in query:
            os.system("taskkill /f /im chrome.exe")
        
        # Play music from a directory
        elif 'play music' in query:
            music_dir = 'E:\Musics'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        
               
        # Close music player
        elif 'close music' in query:
            os.system("taskkill /f /im vlc.exe")
        
        # Get the current time
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        # Shutdown the system
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")
        
        # Restart the system
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        
        # Lock the system
        elif "lock the system" in query:
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif "open notepad" in query:
            npath = "notepad.exe" 
            os.startfile(npath)
        
        # Close Notepad
        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")

        # Open Command Prompt
        elif "open command prompt" in query:
            os.system("start cmd")
        
        # Close Command Prompt
        elif "close command prompt" in query:
            os.system("taskkill /f /im cmd.exe")

        # Open camera
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break
            cap.release()
            cv2.destroyAllWndows()
        
        # Shutdown the assistant
        elif "go to sleep" in query:
            speak('Alright then, I am switching off')
            sys.exit()
        
        # Take a screenshot
        elif "take a screenshot" in query:
            speak('Tell me a name for the file')
            name = takeCommand().lower()
            time.sleep(3)
            img = pyautogui.screenshot() 
            img.save(f"{name}.png") 
            speak("Screenshot saved")
        
        # Perform calculations
        elif "calculate" in query:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready")
                print("Listening...")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                    }[op]
                def eval_bianary_expr(op1,oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("Your result is")
                speak(eval_bianary_expr(*(my_string.split())))
            

        elif "open calculator" in query:
            speak("Opening calculator")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        
        # # Get IP address
        elif "what is my ip address" in query:
            speak("Checking")
            try:
                ipAdd = requests.get('https://api64.ipify.org?format=json').text
                print(ipAdd)
                speak("Your IP address is")
                speak(ipAdd)
            except Exception as e:
                speak("Network is weak, please try again later")
        
        # Volume control
        elif "volume up" in query:
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        
        elif "volume down" in query:
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            
        
        elif "mute" in query:
            pyautogui.press("volumemute")
        
        # Other commands can be added similarly
        
        elif 'type' in query:  # Typing command
            query = query.replace("type", "")
            pyautogui.write(f"{query}")

        elif 'jarvis' in query:
            speak("Yes sir")
        
        
