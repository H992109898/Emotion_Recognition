# -*- coding: UTF-8 -*-

import warnings
from sklearn.externals import joblib
import numpy as np

def get_scores(mind_datas):
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    clf = joblib.load('classifier_mind_wave.pkl')
  
    print mind_datas[1:]
    mind_datas = np.array(mind_datas)
    res = clf.predict(mind_datas)

    return res[0]
    