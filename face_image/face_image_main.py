# -*- coding: UTF-8 -*-

import cv2
import face_rect
import call_back 
import draw_img

def showCamera(mind_datas):
    cap = cv2.VideoCapture(0)
    times = [0.0,]
    emotions = [{},]
    call_back.updata_emotion(emotions, None, times)
    strong_scores = [0, ]
    while(True):
        ret, frame = cap.read()
        faces, gray = face_rect.get_result(frame)
        cv2.setMouseCallback('image', call_back.call_back, [faces, emotions, gray, times, strong_scores, mind_datas,])
        draw_img.draw(faces, emotions[0], strong_scores[0], frame, times[0])
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()