import pywhatkit as kit  #youtube serch
import speech_recognition as s # voice to text 

#convet text to voice
from gtts import gTTS
from playsound import playsound
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


speak("hello Hrsh.. sir.. I am jarvis. What i saerch for you in youtube..")

#create a object of recognition
sr = s.Recognizer()

with s.Microphone() as m:
    print("speak now...")
    audio=sr.record(m,duration=5)
    query = sr.recognize_google(audio,language='eng-in')
    print(" listening you.......")
    print( "you said :-- ",query)

#to shaerch youtube vedio
    kit.playonyt(query)

#text to voice


speak("OK sir..")

