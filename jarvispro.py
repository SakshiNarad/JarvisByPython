import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pywhatkit
from requests import get
import sys





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak("I am Jarvis sir , Please tell me how may I help you")
    

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        
    except Exception as e:
        
        
        print("Say that again please....")
        return "None"
    
    return query

        
            
        
if __name__ == "__main__":
    wishMe()
    #while True:
    if  1:
         query = takeCommand().lower()
         
         if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia","")
             results = wikipedia.summary(query, sentences=2)
                 
             speak("According to Wikipedia")
             print(results)
             speak(results)
         
         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
    
         elif 'open google' in query:
             speak("What should i search on google")
             cm = takeCommand().lower()
             webbrowser.open(f"{cm}")
             
         elif 'open facebook' in query:
             webbrowser.open("facebook.com")
             
             
         elif 'play music' in query:
             music_dir = "C:\\Users\\91762\\Music"
             music = os.listdir(music_dir)
             os.startfile(os.path.join(music_dir,music[0]))
             
         elif 'open command prompt' in query:
             os.system("start cmd")
             
         elif 'the time' in query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"The time is{strTime}")
             
         elif 'open code' in query:
             codePath = "C:\\Users\\91762\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codePath)
             
         elif 'ip address' in query:
             ip = get('https://api.ipify.org').text
             speak(f"your IP address is {ip}")
             
         
         elif "play song on youtube" in query:
             pywhatkit.playonyt("Give Me Some Sunshine")
             
         
         elif "no thanks" in query:
             speak("thanks for using me, have a good day")
             sys.exit()
             
         speak("Thanks for using me, Have a great day ")
             
             
             
         
         
             
             
             
        
             
         