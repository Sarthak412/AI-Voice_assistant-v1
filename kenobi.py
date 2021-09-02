from platform import system
import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sarthak")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sarthak")    

    else:
        speak("Good Evening")
    speak("My name is Kenobi. How may I help you sir.")    

def takeCommand():
    #It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #speak("Listening Sir...")
        print("Listening Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

# email funtion

def Tasks():
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing other tasks
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences= 2)
            speak("Search wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chrome_path = "C://Program Files (x86)//Google//Chrome//Application//Chrome.exe %s"
            webbrowser.get(chrome_path).open("https://youtube.com/")

        elif 'open github' in query:
            chrome_path = "C://Program Files (x86)//Google//Chrome//Application//Chrome.exe %s"
            webbrowser.get(chrome_path).open("https://github.com/")

        elif 'open my linkedin' in query:
            chrome_path = "C://Program Files (x86)//Google//Chrome//Application//Chrome.exe %s"
            webbrowser.get(chrome_path).open("https://linkedin.com/")

        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")   

        elif 'open code' in query:
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open cmd' in query:
            os.system("start cmd")    

        elif 'you can sleep' in query or 'sleep now' in query:
            speak("Wake me if you need help sir.")
            break

if __name__ == "__main__":
    while True:
        permission = takeCommand().lower()
        if "wake up" in permission:
            Tasks()
        elif "turn off" in permission or "turn off kenobi" in permission:
            speak("Goodbye sir.")
            sys.exit()        

