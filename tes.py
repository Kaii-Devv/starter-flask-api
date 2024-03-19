import base64
import json
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MTA3NzE4MDQsImV4cCI6MTcxMDg1ODIwNH0.I9vjxkb7_eZJlflZ9Osszi1JJJztG8D8O3k_TsCgg".split(".")[2]
y=token.replace("-", "+").replace("_", "/")+'='
print(y)
print(len(y)%4)
for x in dir(base64):
    try:
        exec('print(base64.'+x+'(y))')
        print(x)
    except:pass
# print(base64.b64encode(b'{"iat":1710771804,"exp":1741939953}'))

# import datetime


# print((datetime.datetime.now()+datetime.timedelta(days=360)).timestamp())
# #time.time()

