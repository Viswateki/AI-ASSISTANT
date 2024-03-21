import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os

# Initialize pyttsx3 engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

# Function to speak out the given audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

# Main program starts here
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
        # Open Chrome and perform specific actions
        if 'open chrome' in query:
            # Locate and double click on Chrome icon
            img = pyautogui.locateCenterOnScreen('chrome.png')
            pyautogui.doubleClick(img)
            time.sleep(1)
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
            time.sleep(1)
            
            # Click on specific areas and type in text
            img1 = pyautogui.locateCenterOnScreen('edge.png')
            pyautogui.click(img1)
            time.sleep(2)
            img2 = pyautogui.locateCenterOnScreen('brave.png')
            pyautogui.click(img2)
            time.sleep(1)
            # pyautogui.typewrite('', 0.1)
            # pyautogui.press('enter')
            # time.sleep(1)
            pyautogui.press('esc')
            img3 = pyautogui.locateCenterOnScreen('screenshot4.png')
            pyautogui.click(img3)
        
        # Close Chrome
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im brave.exe")

        elif 'close chrome' in query:
            os.system("taskkill /f /im edge.exe")  
