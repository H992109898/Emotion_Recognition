#coding:utf-8
'''
Created on 2017��5��20��

@author: Administrator
'''

from sklearn.externals import joblib
import cv2
import gabor_nn_clf

clf = gabor_nn_clf.gabor_nn_clf()

def get_faces(gray):
    
    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath) 
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 2,
        minSize=(100, 100)
    )
    return faces

def init_data(gray, (x, y, w, h)):
    
    gray = gray[y:y+h, x:x+w]
    gray = cv2.resize(gray, (48, 48))
    gray = cv2.equalizeHist(gray)
    X = gray.reshape((1, 48*48))

    return X

def predict(img, face):
    clf = joblib.load("pipe_nn.pkl")
    X = init_data(img, face)
    #3=Happy, 4=Sad, 5=Surprise, 6=Neutral
    arr = clf.predict_proba(X)[0]
    return [{'scores':{'anger':0.00000001, 'contempt':0.00000002, 
                                   'disgust':0.00000004, 'fear':0.00000003, 
                                   'happiness':arr[0], 'neutral':arr[3], 
                                   'sadness':arr[1], 'surprise':arr[2]}},]
def gabor_predict(img, face):
    scores = clf.predict(img, face)
    return [{'scores':{'anger':0.00000001, 'contempt':0.00000002, 
                                   'disgust':0.00000004, 'fear':0.00000003, 
                                   'happiness':scores['happiness'], 'neutral':scores['neutral'], 
                                   'sadness':scores['sadness'], 'surprise':scores['surprise']}},]
    