# -*- coding: UTF-8 -*-

from face_image import face_image_main
import threading
from mind_wave import read_datas

if __name__ == "__main__":
    mind_datas = [0,0,0,0,0,0,0,0,0]
    threading.Thread(target=face_image_main.showCamera, args=(mind_datas, )).start()
    threading.Thread(target=read_datas.read_datas, args=(mind_datas, )).start()     
    