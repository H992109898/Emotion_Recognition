# -*- coding: UTF-8 -*-

import httplib, urllib, json

        
def get_result(body):
    headers = {
               'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': '983196e52e3d4ae9b16e6c83e446b41d',
               }
    params = urllib.urlencode({})
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", ("/emotion/v1.0/recognize?%s" % params), str(body), headers)
        response = conn.getresponse()
        datas = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
    return json.loads(datas)
    
        
            