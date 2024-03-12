import os
import requests
def encpass(pw,tamp):
    pw = bytearray(pw.encode('utf-8'))
    byter = bytearray(os.urandom(32))
    tamp = bytearray(tamp.encode('utf-8'))
    
    
x = requests.post('https://pyapi.cyclic.app/api/editor/vidio',headers={'content-type': 'application/json; charset=utf-8'},files={'vidio':open('/storage/emulated/0/WhatsApp/Media/WhatsApp Video/VID-20240310-WA0008.mp4','rb')},data={'token':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImF1dGgtdG9rZW4tMDAxIiwidHlwIjoiSldUIn0.eyJzdWIiOiItVFhHamtwRHZHTmJucDIwTExMZSIsImlzcyI6ImZvcnRyZXNzOjp3dzo6cHJkIiwiZXhwIjoxNzEwMjkyMzI5LCJpYXQiOjE3MTAyNjM1MjksIm5iZiI6MTcxMDI2MzUyOSwiaWRwIjoiZW1haWwiLCJqdGkiOiIwZTBjMzUwOS03YjA5LTQ3YmItYjA1OS1jOTJiODA1MzY2MTciLCJhdWQiOiJjb20ubGlnaHRyaWNrcy5FbmxpZ2h0LVZpZGVvOjphOjpwcm9kdWN0aW9uIiwiZW1haWwiOiJpcmpyaHJoaHJqdWV2QDFzZWNtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlfQ.cFQXaPa6lrAx3CBuIFZQgueFzABS1P1Mlv3EkJtWFs720c-Gmw8g-6Gq3xl6qGfChB1e7g6WDtIRv61OELoluUG1tbmE-oAMN-udLJnkRIMSwvqtoEUH_NLIOyf3KvtzNITJc9wOXeLZxRuMcIwY8yEhqFP2WkxPBKIkMhpCovfIEHJLYECPljcWEuzO9hRkHJoBQ3feM0DA94yUeDx_rj9LEuvIN9SYXiIikqtwID7xcX7m05PFqRmvTdS-yCSS2r6J99qXs-KIQML9vf-pMyL-HWiVgL_P2QjCjxTo-gEPdr5mZxEGsANmIZE_b7v2T4OQSExHMVnix6vapg1XFQ','prompt':'snow, morning'})
print(x.text)