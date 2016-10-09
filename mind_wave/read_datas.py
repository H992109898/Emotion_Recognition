# -*- coding: UTF-8 -*-

import ctypes
import time
import threading

def read_datas(mind_data):
    dll=ctypes.CDLL('get_brain_wave.dll')
    
    data = (ctypes.c_int*10)()
    isquit = (ctypes.c_bool*2)()
    isquit[0] = False
    
    #传入一个数组data长度大于8
    read = threading.Thread(target=dll.get_brain_wave, args=(data, isquit, ))
    read.start()
    
    lock = threading.Lock() 
    
    raw_last_value = 0
    count_same = 0
    count_time = 1
    
    while(1):
        lock.acquire()
        for i in range(9): 
            mind_data[i] = data[i]
        lock.release()
        
        if data[0] == raw_last_value:
            count_same += 1
        else:
            count_same = 0
            
            count_time += 1
            
        raw_last_value = data[0]
        
        if count_same > 10:
            break
          
        time.sleep(1)
    isquit[0] = True
    print "mind wave quit!"
    