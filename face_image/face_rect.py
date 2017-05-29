# -*- coding: UTF-8 -*-

import cv2

def get_result(img, faceCascade):
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 2,
        minSize=(170, 170)
    )
    return faces

