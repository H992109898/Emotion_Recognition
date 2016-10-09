# -*- coding: UTF-8 -*-

import cv2, time
import calcul_emotion
import threading
from mind_wave import mind_wave_main

def inRect(x, y, face):
    LT_x = face[0]
    LT_y = face[1]
    RD_x = face[0] + face[2]
    RD_y = face[1] + face[3]
    return x > LT_x and x < RD_x and y > LT_y and y < RD_y

#param [faces, emotions, gray, times, strong_scores, mind_datas]
def call_back(event, x, y, flags, param):
    try:
        face = param[0][0]
    except IndexError:
        return
    if event==cv2.EVENT_LBUTTONDOWN and inRect(x, y, face):
        threading.Thread(target=updata_emotion, args=(param[1], param[2], param[3])).start()
        param[4][0] = mind_wave_main.get_scores.get_scores(param[5])
        
        
def updata_emotion(emotions, img, times):
    
    body = get_body(img)
    data = calcul_emotion.get_result(body)
    print data
    
    lock = threading.Lock() 
    lock.acquire()
    try:
        emotions[0] = data[0]['scores']
        times[0] = time.time()
    except:
        print "face no found"
    lock.release()

def get_body(img):
    fileName = "suffer.jpg"
    cv2.imwrite(fileName, img)
    fout = open(fileName, "rb")
    data = fout.read()
    fout.close()
    return data