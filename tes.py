import os
import requests
def encpass(pw,tamp):
    pw = bytearray(pw.encode('utf-8'))
    byter = bytearray(os.urandom(32))
    tamp = bytearray(tamp.encode('utf-8'))
    
    
x = requests.post('https://pyapi.cyclic.app/api/editor/vidio',files={'video':bytesVideo},data={'token':'e','prompt':'morning'})
print(x.text)