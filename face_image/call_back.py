# -*- coding: UTF-8 -*-

import cv2, time
from face_image import calcul_emotion

def inRect(x, y, face):
    LT_x = face[0]
    LT_y = face[1]
    RD_x = face[0] + face[2]
    RD_y = face[1] + face[3]
    return x > LT_x and x < RD_x and y > LT_y and y < RD_y

def emotion(event, x, y, flags, param):
    try:
        face = param[0][0]
    except IndexError:
        print "face no found"
        return
    if event==cv2.EVENT_LBUTTONDOWN and inRect(x, y, face):
        body = get_body(param[2])
      
        data = calcul_emotion.Calcul().get_result(body)
        print data
        if len(data) > 0:
            param[1][0] = data[0]['scores']
            param[3][0] = time.time()
        else:
            print "face no found"
            
def get_body(img):
    fileName = "suffer\\1.jpg"
    cv2.imwrite(fileName, img)
    fout = open(fileName, "rb")
    data = fout.read()
    fout.close()
    return data