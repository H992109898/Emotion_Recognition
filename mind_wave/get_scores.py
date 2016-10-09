# -*- coding: UTF-8 -*-

from sklearn.externals import joblib
import numpy as np

def get_scores(mind_datas):
    clf = joblib.load('classifier_mind_wave.pkl')
    print mind_datas
    mind_datas = np.array(mind_datas)
    res = clf.predict(mind_datas)

    return res[0]
    