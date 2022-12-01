from turtle import speed
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")    

    else:
        speak("Good Evening!")    
    speak("I am your PC. please tell me how can I help you.")
    
    

def takecommand():
# It takes microphone input from user and return a string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()

    # logic for executing tasks

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
      
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            print(" The time is", strtime)
            speak(f"sir, the time is {strtime}")

        elif 'open virtual studio code' in query:
            codepath = "C:\\Users\\BHUPENDRA SINGH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open vlc media player' in query:
            vlcpath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            os.startfile(vlcpath)
            
        elif 'open chrome' in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        elif 'open spotify' in query:
            spotifypath = "C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.147.684.0_x86__zpdnekdrzrea0\\Spotify.exe"
            os.startfile(spotifypath)
   
        elif 'exit'  in query:
            speak("I am enjoying to be with you ")
            speak("Thank u and Have a good day sir.")
            exit()

        elif 'quit' in query:
            speak("I am enjoying to be with you ")
            speak("Thank u and Have a good day sir.")
            exit()

        elif 'shutdown' in query:
            speak("I am enjoying to be with you ")
            speak("But it is your wish to leave.")
            speak("Thank u and Have a good day sir.")
            exit()
        elif 'shut up' in query:
            speak("ohhk, may be you are angry at the moment.")

        elif 'open internet speed test' in query:
            speak("On it,, Sir")
            internetstest = "D:\\New folder\\My Project\\Internert Speed Tester\\speedtester.py"
            os.startfile(internetstest)
            


        elif 'open the vitual keyboard' in query:
            speak("On it, sir")
            vitualkeyboard = ""

        elif 'shut up' in query:
            speak("ohhk, may be you are angry at the moment.")

        elif 'shut up' in query:
            speak("ohhk, may be you are angry at the moment.")
            