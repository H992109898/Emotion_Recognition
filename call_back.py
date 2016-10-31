# -*- coding: UTF-8 -*-

import cv2
from face_image import calcul_emotion
import threading
import mind_wave
import os
from face_image import Animation

def inRect(x, y, face):
    LT_x = face[0]
    LT_y = face[1]
    RD_x = face[0] + face[2]
    RD_y = face[1] + face[3]
    return x > LT_x and x < RD_x and y > LT_y and y < RD_y

#param [faces, img, mind_datas]
def call_back(event, x, y, flags, param):
    try:
        face = param[0][0]
    except IndexError:
        return
    img = param[1]
    mind_datas = param[2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    emotions = [{},]
    if event==cv2.EVENT_LBUTTONDOWN and inRect(x, y, face):
        threading.Thread(target=updata_emotion, args=(emotions, gray)).start()
        isStrong = mind_wave.get_scores.get_scores(mind_datas)
        color = {1: (0, 0, 255),
             0: (0, 255, 0),
            -1: (255, 0, 0)
            }[isStrong]
        play = Animation.Animation(img, face, 'image', emotions, color)
        play.play()
        
def updata_emotion(emotions, img):
    
    body = get_body(img)
    data = calcul_emotion.get_result(body)
    
    lock = threading.Lock() 
    lock.acquire()
    try:
        emotions[0] = data[0]['scores']
    except:
        pass

    lock.release()
    

def get_body(img):
    fileName = "suffer.jpg"
    cv2.imwrite(fileName, img)
    fout = open(fileName, "rb")
    data = fout.read()
    fout.close()
    
    try:
        os.remove('suffer.jpg')
    except:
        pass
    return data