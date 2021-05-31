import datefinder
import winsound
import datetime
from pygame import *
import pygame

pygame.mixer.init()

pygame.mixer.music.load('E:\\jarvis ai\\Alarm.mp3')


def alarm(text):
    timea = datefinder.find_dates(text)
    for mat in timea:
        print(mat)
    string = str(mat)
    timea = string [11:]
    houra =timea[:-6]
    houra = int(houra)
    mina =timea[3:-3]
    mina = int(mina)

    while True:
        print("your alarm is start")
        if houra == datetime.datetime.now().hour:
            if mina == datetime.datetime.now().minute:
                print("runing")
                # pygame.mixer.music.play()
                # pygame.mixer.music.play()
                winsound.PlaySound('E:\\jarvis ai\\Alarm.mp3',winsound.SND_LOOP)
            elif mina<datetime.datetime.now().minute:
                break

alarm("set alarm at 8:03 pm")