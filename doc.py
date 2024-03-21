import speech_recognition as sr
import docx
import requests
from bs4 import BeautifulSoup

def fetch_info(topic):
    # Search for information about the given topic on Wikipedia
    url = f"https://en.wikipedia.org/wiki/{topic}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Find the main content of the Wikipedia page
    content = soup.find("div", {"id": "mw-content-text"})
    paragraphs = content.find_all("p")
    # Extract text from the paragraphs
    text = "\n".join([p.text for p in paragraphs])
    return text

def create_document(text, filename):
    # Create a new Word document
    doc = docx.Document()
    # Add the fetched text to the document
    doc.add_paragraph(text)
    # Save the document with the given filename
    doc.save(filename)

def voice_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    while True:
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            print("Listening...")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            # Listen for the command
            audio = recognizer.listen(source)
            
        try:
            # Recognize the command from the audio
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            # Check if the user wants to exit
            if "exit" in command.lower():
                return None
            else:
                return command
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print("Error occurred; {0}".format(e))

def main():
    while True:
        # Get the voice command
        topic = voice_to_text()
        
        # Check if the user wants to exit
        if topic is None:
            print("Exiting...")
            break
        
        # Fetch information about the given topic
        info = fetch_info(topic)
        
        # Create a Word document with the fetched information
        filename = f"{topic}.docx"
        create_document(info, filename)
        print(f"Document '{filename}' created successfully!")

if __name__ == "__main__":
    main()
