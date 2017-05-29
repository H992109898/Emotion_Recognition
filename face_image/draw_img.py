# -*- coding: UTF-8 -*-

import cv2

def draw(faces, img, windowName):
       
    text = "click face rectangles to get emotion."
    cv2.putText(img, text, (180, 100), 0, 0.5, (0, 2, 15),0)
        
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break
    cv2.imshow(windowName, img)
     
        