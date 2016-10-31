# -*- coding: UTF-8 -*-

import cv2
import face_rect
import call_back
import draw_img

def showCamera(mind_datas):
    cap = cv2.VideoCapture(0)

    windowName = 'image'
    while(True):
        ret, frame = cap.read()
        if ret is not True:
            print "no found camera"
            
        faces = face_rect.get_result(frame)
        
        cv2.setMouseCallback('image', call_back.call_back, [faces, frame, mind_datas])
        draw_img.draw(faces, frame, windowName)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()