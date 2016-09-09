# -*- coding: UTF-8 -*-

import cv2
from face_image import face_rect, call_back, draw_img
                    

if __name__ == "__main__":
    
    cap = cv2.VideoCapture(0)
    emotions = [{},]
    times = [0.0,]
    while(True):
        ret, frame = cap.read()
        faces, gray = face_rect.Face_rect().get_res(frame)
        cv2.setMouseCallback('image', call_back.emotion, [faces, emotions, gray, times])
        draw_img.draw(faces, emotions[0], frame, times[0])
        if cv2.waitKey(1) & 0xFF == 27:
            break
         
    cap.release()
    cv2.destroyAllWindows()
    