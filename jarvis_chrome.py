import pyttsx3
import speech_recognition as sr
import pyautogui
import time
import os
import keyboard

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
        r.pause_threshold = 1
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
        
        # Open Chrome
        if 'open chrome' in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        
        # Maximize the current window
        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')
        
        # Google search
        elif 'google search' in query:
            query = query.replace("google search", "")
            pyautogui.hotkey('alt', 'd')
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        
        # YouTube search
        elif 'youtube search' in query:
            query = query.replace("youtube search", "")
            pyautogui.hotkey('alt', 'd')
            time.sleep(1)
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(1)
            pyautogui.write(f"{query}", 0.1)
            pyautogui.press('enter')
        
        # Open a new window
        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open mic' in query:
            keyboard.press_and_release('windows+h')
            
        
        # Open an incognito window
        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')
        
        # Minimize the current window
        elif 'minimize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')
        
        # Open browsing history
        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')
        
        # Open downloads
        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')
        
        # Switch to previous tab
        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')
        
        # Switch to next tab
        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')
        
        # Close current tab
        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')
        
        # Close current window
        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')
        
        # Clear browsing history
        elif 'clear browsing history' in query:
            pyautogui.hotkey('ctrl', 'shift', 'delete')
        
        # Close Chrome
        elif 'close chrome' in query:
            os.system("taskkill /f /im chrome.exe")

       
