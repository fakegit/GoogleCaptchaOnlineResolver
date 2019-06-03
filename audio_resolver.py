#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from datetime import datetime
import requests,re,threading,time
import ctypes
from msvcrt import getch
from collections import deque
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from colorama import init
from colorama import Fore, Back, Style
import json
from threading import *
screen_lock = Semaphore(value=1)




# Pass the audio data to an encoding function.
def encode_audio(audio):
  audio_content = audio.read()
  return base64.b64encode(audio_content)

while 1:

    url=input("\nInsert url of the audio: ")

#download audio file
    s = requests.Session() 
    audio=s.get(url,  allow_redirects=True)
#     open('audio_challange.tmp', 'wb').write(audio.content)
# 
#     fh=open('audio_challange.tmp', 'rb')
# 
# 
#     audio_wav=open('audio_challange.tmp', 'r')
#audio_to_send=encode_audio(audio_wav)
#     audio_text=open('base64.txt', 'w')
#     audio_text_raw=open('raw.txt', 'wb')
# audio_text.write(encode_audio(audio_wav))
#print(audio_to_send)



#upload audio
    headers= {
              'Content-Type': "text/plain;charset=UTF-8",
              'DNT' : '1',
              'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
              'Referer': 'https://cloud.google.com/speech-to-text/',    
              'Origin': 'https://cloud.google.com',
              }


    data2= { "config":    {
             "enableAutomaticPunctuation":"false",
             #"encoding":"LINEAR16",
             "languageCode":"it-IT",
             #"sampleRateHertz":48000,
             "model":"command_and_search"
                        },
             "audio":      {
                 "content": base64.standard_b64encode(audio.content).decode('utf-8')
                 }
             }




    r = requests.post("https://cxl-services.appspot.com/proxy?url=https%3A%2F%2Fspeech.googleapis.com%2Fv1p1beta1%2Fspeech%3Arecognize",  json=data2,headers = headers)
#   audio_text.write(r.text)
#   print("sending audio\n")
#	print(r.text)
    data=r.json()
    captcha=data['results'][0]['alternatives'][0]['transcript']
    confidance=data['results'][0]['alternatives'][0]['confidence']
    captcha=captcha.replace(" ", "")
    print("Captcha is:%s, Confidance is:%s"%(captcha,confidance))



    print("\n\nDone")