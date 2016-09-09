# -*- coding: UTF-8 -*-

import cv2

class Face_rect(object):
    
    def get_res(self, img):
        cascPath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(cascPath)
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 3,
            minSize=(80, 80)
        )
        return faces, gray

