# -*- coding: UTF-8 -*-

import httplib, urllib, json

class Calcul(object):
    
    def __init__(self):
        self.headers = {
                # Request headers
               'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': '983196e52e3d4ae9b16e6c83e446b41d',
               }
        self.params = urllib.urlencode({})
        
    def get_result(self, body):
        try:
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            conn.request("POST", ("/emotion/v1.0/recognize?%s" % self.params), str(body), self.headers)
            response = conn.getresponse()
            datas = response.read()
            conn.close()
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        return json.loads(datas)
    
        
            