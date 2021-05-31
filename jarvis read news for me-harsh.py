from win32com.client import Dispatch
import requests
import json
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# Translator:
def translation (info,des):
    translator = Translator()
    translated_sentence = translator.translate(info,dest=des)
    try :
        print(translated_sentence.pronunciation)
        convert_to_audio(translated_sentence.text)
    except Exception as e:
        print(e)

# speak audio
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


def play_audio(path_of_audio):
    playsound(path_of_audio)
def convert_to_audio(str):
    my_audio = gTTS(str)
    my_audio.save('hello.mp3')
    play_audio('hello.mp3')
    os.remove('hello.mp3')

#sub..    
if __name__ == '__main__':
    
    speak("hello.. sir am jarvis. on which subject I read news for you.. please tell me.. The subjects are given below")
print("subjects are :-- headlines, business, health, sports, Technology")


    

#sub.. 
api_dict = {"headlines": "https://newsapi.org/v2/top-headlines?country=in&apiKey=78edbcf89bd24bcebe4233f37515a00d",
            "business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=78edbcf89bd24bcebe4233f37515a00d",
            
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=78edbcf89bd24bcebe4233f37515a00d",
            "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=78edbcf89bd24bcebe4233f37515a00d",
            "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=78edbcf89bd24bcebe4233f37515a00d"}
content = None
url=None
input_api = input("types:--")
for key,value in api_dict.items():
    if key in input_api.lower():
        url = value
        print(url)
        print("url found")
        break
    else:
        url = True

#lang.
if __name__ == '__main__':
    speak("OK Sir.. in which language I read news.. Hindi. or.. English ")

    lang_dict = {"hindi":"hi", "english":"en","gujarati":"gu"}
    lang = None
    # print("listening...")
    lang_in = input("types:--")
   
    for key,value in lang_dict.items():
        if key.lower() in lang_in.lower():
            lang = value
            print(lang)
            print("lang found")
            break
        else:
            lang = True

    if lang is True:
        print("lang not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("live news for today.")
    arts = news['articles']
    for articles in arts:
        article = articles['title']
        speak("Moving  to the next news.. ")
        news_url = articles['url']
        if article is None:
            continue
        translation(article,lang)
        print(f"for more onformation visit : {news_url}\n")
    print("Thank you!!")
a = input("Entre for close ")
