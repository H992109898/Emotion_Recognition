from sklearn.externals import joblib
import dlib
import numpy as np
import cv2
from itertools import product

class gabor_nn_clf(object):
    
#     pack for predict 4 emotion
#     3:happiness
#     4:sadness
#     5:surprise
#     6:natural


    clf = joblib.load("pipe_nn_garbor.pkl")
    PREDICTOR_PATH = "shape_predictor_68_face_landmarks.dat"
    predictor = dlib.shape_predictor(PREDICTOR_PATH)
    
    def build_filters(self):
        filters = []
        ksizes = [4, 8]
        for ksize in ksizes:
            for theta in np.arange(0, np.pi, np.pi / 8):
                params = {'ksize':(ksize, ksize), 'sigma':1.0, 'theta':theta, 'lambd':5.0,
                          'gamma':0.02, 'psi':0, 'ktype':cv2.CV_32F}
                kern = cv2.getGaborKernel(**params)
                kern /= 1.5*kern.sum()
                filters.append((kern,params))
    
        return filters

    def process(self, img, filters):
        results = []
        for kern,params in filters:
            fimg = cv2.filter2D(img, cv2.CV_8UC3, kern)
            results.append(fimg)
        return results   
    
    def gabor(self, img):
        filters = self.build_filters()
        imgs = np.array(self.process(img, filters))
        
        return imgs
    
    def init_data(self, img, (x, y, w, h)):
        img = img[y:y+h, x:x+w]
        img = cv2.resize(img, (48, 48))
        img = cv2.equalizeHist(img)
        imgs = self.gabor(img)
        imgs = imgs.reshape((16, 48, 48))
        rect = dlib.rectangle(0, 0, 48, 48)
        landmarks = np.array([[p.x,p.y] for p in self.predictor(img, rect).parts()])  
              
        x = np.zeros(1088)
        for idx, (point, img) in enumerate(product(landmarks, imgs)):
            left = 47 if point[0] > 47 else point[0]
            top = 47 if point[1] > 47 else point[1]
            x[idx] = img[top][left]
             
        #x = np.append(geometry_x, x, axis = 0)
        X = []
        X.append(x)
        return np.array(X)
    def predict(self, img, face):
        X = self.init_data(img, face)
    
        #3=Happy, 4=Sad, 5=Surprise, 6=Neutral
        arr = self.clf.predict_proba(X)[0]
        print arr
        return {'happiness':arr[0], 'neutral':arr[3], 
             'sadness':arr[1], 'surprise':arr[2]}
        