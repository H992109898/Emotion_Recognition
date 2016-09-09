# -*- coding: UTF-8 -*-

import cv2, time

class draw(object):

    def __init__(self, faces, emotion, img, pre_time):
        text = "click face rectangles to get emotion."
        cv2.putText(img, text, (180, 100), 0, 0.5, (0, 2, 15),0)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if time.time() - pre_time < 3: 
                scores = emotion
                self.draw_scores(img, scores, x+w, y)
                self.draw_emotion(img, scores, x + w/2, y)
            break
        cv2.imshow('image', img)
        
    def draw_scores(self, img, scores, x, y):
        i = 15
        for emotion in scores:
            text = emotion + ': ' + str(scores[emotion])
            cv2.putText(img, text, (x, y+i), 0, 0.5, (255,255,200),0)
            i += 15
    
    def draw_emotion(self, img, scores, x, y):
        main_emotion = ""
        max_score = 0.0
        for emotion in scores:
            if max_score < scores[emotion]:
                max_score = scores[emotion]
                main_emotion = emotion
        
        cv2.putText(img, main_emotion, (x-45, y-15), 0, 0.5, (255,255,200),0)
        
    
     
        