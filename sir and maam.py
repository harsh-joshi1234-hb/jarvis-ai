import pywhatkit as kit  #youtube serch
import speech_recognition as s # voice to text. pip install SpeechRecognition 


#convet text to voice 
from gtts import gTTS
from playsound import playsound


#for sir and maam

def play_audio(path_of_audio):
    playsound(path_of_audio)
def convert_to_audio(text):
    my_audio = gTTS(text)
    my_audio.save('Sir.mp3')
    play_audio('Sir.mp3')
def convert_to_audio_1(text):
    my_audio = gTTS(text)
    my_audio.save('Sir_1.mp3')
    play_audio('Sir_1.mp3')
convert_to_audio("hello  Sir.. I am jarvis. What i saerch for you in youtube..")






#create a object of recognition -- pip install Speech Recognition
sr = s.Recognizer()

with s.Microphone() as m:
    print("speak now...")
    audio=sr.record(m,duration=5)
    query = sr.recognize_google(audio,language='eng-in')
    print(" listening you.......")
    print( "you said :-- ",query)

#to shaerch youtube vedio
    kit.playonyt(query)



from win32com.client import Dispatch # pip install pywin32
speak = Dispatch("SAPI.SpVoice")


speak.Speak("OK. sir.")



