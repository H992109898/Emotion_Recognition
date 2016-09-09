# -*- coding: UTF-8 -*-

import cv2, time, thread
import calcul_emotion

def inRect(x, y, face):
    LT_x = face[0]
    LT_y = face[1]
    RD_x = face[0] + face[2]
    RD_y = face[1] + face[3]
    return x > LT_x and x < RD_x and y > LT_y and y < RD_y

#param [faces, emotions, gray, times]
def call_back(event, x, y, flags, param):
    try:
        face = param[0][0]
    except IndexError:
        return
    if event==cv2.EVENT_LBUTTONDOWN and inRect(x, y, face):
        thread.start_new(updata_emotion, (param[1], param[2], param[3]))
        
def updata_emotion(emotions, img, times):
    body = get_body(img)
    data = calcul_emotion.get_result(body)
    print data
    try:
        emotions[0] = data[0]['scores']
        times[0] = time.time()
    except:
        print "face no found"

def get_body(img):
    fileName = "suffer.jpg"
    cv2.imwrite(fileName, img)
    fout = open(fileName, "rb")
    data = fout.read()
    fout.close()
    return data