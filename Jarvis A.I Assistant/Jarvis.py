import os

import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio

engine = pyttsx3.init('sapi5') #sapi5 is the technology use in this program
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        speak("Hello Sir Jay, How can i help you?")
        print("Listening...")                 
        speak("...")
        speak("...")
        speak("...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        speak("Just Wait for few Moments Sir...")
        print("Wait for few Moments...")
        query=r.recognize_google(audio, language='en-in')
        print(f"You just said: {query}\n")
    except Exception as e:
        print(e)
        speak("Please Tell me Again")
        query="none"
    return query

def wishings():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif (hour >= 12 and hour < 17):
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif (hour >= 17 and hour < 21):
        print("Good Morning Sir")
        speak("Good Morning Sir")
    else:
        print("Good Night Sir")
        speak("Good Night Sir")

if __name__ == "__main__":
    wishings()
    query=commands().lower()
    if('time' in query):
        strTime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print(strTime)
    #elif('open helmet heroes' or 'open heroes' or 'open helmet' in query):
        #speak("Opening Helmet-heroes Application sir...")
        #os.startfile("C:\\Program Files (x86)\\Helmet Heroes\\Helmet Heroes.exe")
    elif('lights' or 'turn on  the lights' or 'turn the lights on' in query):
        speak("Turning ON the lights sir...")
        speak("...")
        speak("...")
        speak("...")
        speak("Your, Welcome Sir!")


#speak("Hello Sir Jay, How can i help you?")
#speak("Sir, Today is Fest of virgin mary de regla...")




