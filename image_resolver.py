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

    url=input("\nInsert url of the image: ")
    s = requests.Session() 
    image=s.get(url)


    headers= {
              'Content-Type': "text/plain;charset=UTF-8",
              'DNT' : '1',
              'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
              'Referer': 'https://cloud.google.com/vision/',    
              'Origin': 'https://cloud.google.com',
              }
 
  
    data2= {"requests":
     [{"image":{"content":base64.standard_b64encode(image.content).decode('utf-8')},
       "features":[{"type":"TYPE_UNSPECIFIED","maxResults":50},{"type":"LANDMARK_DETECTION","maxResults":50},{"type":"FACE_DETECTION","maxResults":50},{"type":"LOGO_DETECTION","maxResults":50},{"type":"LABEL_DETECTION","maxResults":50},{"type":"DOCUMENT_TEXT_DETECTION","maxResults":50},{"type":"SAFE_SEARCH_DETECTION","maxResults":50},{"type":"IMAGE_PROPERTIES","maxResults":50},{"type":"CROP_HINTS","maxResults":50},{"type":"WEB_DETECTION","maxResults":50}],
       "imageContext":{"cropHintsParams":{"aspectRatios":[0.8,1,1.2]}}}]}
 
 
    r = requests.post("https://cxl-services.appspot.com/proxy?url=https%3A%2F%2Fvision.googleapis.com%2Fv1%2Fimages%3Aannotate",  json=data2,headers = headers)

    data=r.json()
    try:
        captcha=data['responses'][0]['fullTextAnnotation']['text']
        print("Captcha is:%s"%captcha)
    except:
        pass
        




    print("\n\nDone")