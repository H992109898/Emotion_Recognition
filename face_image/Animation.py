# -*- coding: UTF-8 -*-

import cv2


class Animation:
    
    def __init__(self, img, face, windowName, emotionDate, color):
        self.img = img
        self.face = face
        self.logo = ''
        self.faceRect = img[face[1]:(face[1]+face[3]), face[0]:(face[0]+face[2])].copy()
        self.windowName = windowName
        self.emotionDate = emotionDate
        self.color = color
    
    def toGray(self, img):
        for row in img:
            for ele in row:
                ele[0] = ele[1]
                ele[2] = ele[1]
                
    def showGray(self):
        #灰度化
        gray = self.img
        self.toGray(gray)
        gray[self.face[1]:(self.face[1]+self.face[3]), self.face[0]:(self.face[0]+self.face[2])] = self.faceRect
        cv2.imshow(self.windowName, gray)
        cv2.waitKey(1800)
        
    def showBiggerFace(self):
        for i in range(31):
            self.faceRect = cv2.resize(self.faceRect, (200 + 10*i, 200 + 10*i))
            cv2.imshow(self.windowName, self.faceRect)
            cv2.waitKey(25)
    
    def getMainEmotion(self):
        
        main_emotion = ""
        max_score = 0.0
        #cv2.waitKey(1000)
       
        if len(self.emotionDate[0]) == 0:
            self.emotionDate[0] = {'anger':0.00000001, 'contempt':0.00000002, 
                                   'disgust':0.00000004, 'fear':0.00000003, 
                                   'happiness':0.00000005, 'neutral':0.99999970, 
                                   'sadness':0.000000006, 'surprise':0.00000009}
        for emotion in self.emotionDate[0]:
            if max_score < self.emotionDate[0][emotion]:
                max_score = self.emotionDate[0][emotion]
                main_emotion = emotion
        
        print self.emotionDate[0]
        path = r'resourse\\' + main_emotion + r'_cartoon.jpg'
        print path
        self.logo = cv2.imread(path)
        return main_emotion
    
    def showText(self, xPos, yPos):
        text = self.getMainEmotion();
        cv2.putText(self.finalImg, text, (xPos, yPos), 5, 3.5, self.color,0)
        
        text = 'Facial expression score:'
        cv2.putText(self.finalImg, text, (525, 50), 1, 1.25, self.color,0)
        i = 50
        for emotion in self.emotionDate[0]:
            text = emotion + ': ' + str(self.emotionDate[0][emotion])
            cv2.putText(self.finalImg, text, (525, 50+i), 1, 1.25, self.color,0)
            i += 50
        
    def showMixROI(self):

        #感兴趣区域图像混合
        self.logo = cv2.resize(self.logo, (500, 500))
        for i in range(10):
            self.finalImg[0:500, 0:500] = cv2.addWeighted(self.faceRect, 1-0.06*i, self.logo, i*0.06, 0)
            cv2.imshow(self.windowName, self.finalImg)
            cv2.waitKey(200)
        
    def showFinalImg(self):
        #显示参数
        self.finalImg = cv2.resize(self.faceRect, (800, 650))
        self.finalImg[0:500, 0:500] = self.faceRect
        self.finalImg[500:650, 0:800] = 0
        self.finalImg[0:500, 500:800] = 0
        for i in range(31):
            cv2.imshow(self.windowName, self.finalImg[0:500+i*5, 0:500+i*10])
            cv2.waitKey(30)

        self.showText(50, 575)
        cv2.waitKey(1000)
        
        self.showMixROI()
        cv2.waitKey(3000)
        
    def play(self):
        self.showGray()
        self.showBiggerFace()
        self.showFinalImg()
    