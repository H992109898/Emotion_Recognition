# -*- coding: UTF-8 -*-

import cv2
from face_image import face_rect, call_back, draw_img
                    
def showCamera():
    cap = cv2.VideoCapture(0)
    emotions = [{},]
    times = [0.0,]
    call_back.updata_emotion(emotions, None, times)
    while(True):
        ret, frame = cap.read()
        faces, gray = face_rect.get_result(frame)
        cv2.setMouseCallback('image', call_back.call_back, [faces, emotions, gray, times])
        draw_img.draw(faces, emotions[0], frame, times[0])
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    showCamera()
    
         
    