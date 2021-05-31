# google saerch with input
# import webbrowser # open google
# c= input()
# webbrowser.open('https://google.com/?#q='+ c)
#-----end---


#google search  with speaking
import webbrowser # open google
import speech_recognition as s # voice to text 

#convet text to voice
from gtts import gTTS
from win32com.client import Dispatch
from playsound import playsound

def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


speak("hello Harsh.. sir.. I am jarvis. What i saerch for you in google..")

#create a object of recognition
sr = s.Recognizer()

with s.Microphone() as m:
    print("speak now...")
    audio=sr.record(m,duration=5)
    query = sr.recognize_google(audio,language='eng-in')
    print(" listening you.......")
    print( "you said :-- ",query)

#to shaerch google

    webbrowser.open('https://google.com/?#q='+ query)


speak("OK sir..")

