# -*- coding: UTF-8 -*-

import httplib, urllib, json

        
def get_result(body):
    headers = {
               'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': '983196e52e3d4ae9b16e6c83e446b41d',
               }
    params = urllib.urlencode({})
    
    cntTime = 0
    while cntTime < 10:
        try:
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            conn.request("POST", ("/emotion/v1.0/recognize?%s" % params), str(body), headers)
            response = conn.getresponse()
            datas = response.read()
            conn.close()
            break
        except Exception as e:
            cntTime += 1
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
            pass
    '''
    try:
        print datas[0]
    except:
        print "no datas"
    '''
    return json.loads(datas)
    
        
