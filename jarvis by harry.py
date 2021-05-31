import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as kit  #youtube serch
import alarm

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    speak("I am Jarvis . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("OK Sir.")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("OK Sir.")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("OK Sir.")
            webbrowser.open("stackoverflow.com")   

        elif 'read news' in query:
            speak("OK Sir.")

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
            
                
            speak("on which subject I read news for you.. please tell me.. The subjects are given below")
            print("subjects are :-- headlines, business, health, sports, Technology")


                

            #sub.. 
            api_dict = {"headlines": "https://newsapi.org/v2/top-headlines?country=in&apiKey=78edbcf89bd24bcebe4233f37515a00d",
                        "business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=78edbcf89bd24bcebe4233f37515a00d",
                        
                        "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=78edbcf89bd24bcebe4233f37515a00d",
                        "technology" : "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=78edbcf89bd24bcebe4233f37515a00d",
                        "health":"https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=78edbcf89bd24bcebe4233f37515a00d"}
            content = None
            url=None
            input_api = query = takeCommand().lower()
            for key,value in api_dict.items():
                if key in input_api:
                    url = value
                    print(url)
                    print("url found")
                    break
                else:
                    url = True

            #lang.
            
            speak("OK Sir.. in which language I read news.. Hindi. or.. English ")

            lang_dict = {"hindi":"hi", "english":"en","gujarati":"gu"}
            lang = None
            # print("listening...")
            lang_in = query = takeCommand().lower()
        
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
                    print(f"for more information visit : {news_url}\n")
                print("Thank you!!")


        elif 'search in google' in query:
            query = takeCommand().lower()
            speak("OK Sir. What I search for you in google")
            webbrowser.open('https://google.com/?#q='+ query)
        
        elif 'search in youtube' in query:
            query = takeCommand().lower()
            speak(" OK Sir. What I search for you in google")
            kit.playonyt(query)   



        elif 'play music' in query:
            speak("OK Sir.")
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #     codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)

        elif 'email to harsh' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harsh. I am not able to send this email")    
        

        elif 'alarm' in query:
            alarm.alarm(query)