import base64
token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImJhNjI1OTZmNTJmNTJlZDQ0MDQ5Mzk2YmU3ZGYzNGQyYzY0ZjQ1M2UiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQklTS0lNQSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLcTFMN09MSEZLQlN0Z1FubzBUeFJoMWFONC1SVFB5VGhhRF9aX0o0US09czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY3V0ZWNoYXQtMWQwNWYiLCJhdWQiOiJjdXRlY2hhdC0xZDA1ZiIsImF1dGhfdGltZSI6MTcxMTY5MjgyNiwidXNlcl9pZCI6IktHV0NYSTVka1dWdXhrTDB1R0ZFbFVrQWNhejEiLCJzdWIiOiJLR1dDWEk1ZGtXVnV4a0wwdUdGRWxVa0FjYXoxIiwiaWF0IjoxNzExNjkyODI2LCJleHAiOjE3MTE2OTY0MjYsImVtYWlsIjoiY2VtaWxhbmlubkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMTUzNTc2NjIxODg0NTI2NDc3MyJdLCJlbWFpbCI6WyJjZW1pbGFuaW5uQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.C__3D3UFsU_NSVFGjCDKOe9Gn32omuk8pzNkA4oZizY2k_G75sukD8uRZas28eVXKbX2_QtKdNWxY0z9fpU4FrVWu3LmX-OecqO-AbvxZQEDdB0ie1xG_PHbxYf-B6tOgjp3bqysfI029p2yH5LAa-WTFu_6n769pShxr65-cntiYv9luQPHNInA6kSD3z7dQXM2BiyOeFAudeKUd-7TcGa1zvj8g7InITsB47aei8qKmNUpg8aeMZVYobsTmP7JZce9DpLMJPof5ApUbpDQCZidUb5DdyDnVtb1evoA63GhOMe1bxujT9v6zvF_ctlJirqmZ0quKBktfN_XJppAGg'

for x in token.split('.') :
    try:
        print(base64.b64decode(eval("b'"+x+"='")))
    except:
        try:
            print(base64.b64decode(eval("b'"+x+"=='")))
        except Exception as e:
            print(e)
import datetime

# Konversi waktu pembuatan token
iat_timestamp = 1711682161
iat_datetime = datetime.datetime.utcfromtimestamp(iat_timestamp)
print("Waktu pembuatan token:", iat_datetime)

# Konversi waktu kedaluwarsa token
exp_timestamp = 1711685761
exp_datetime = datetime.datetime.utcfromtimestamp(exp_timestamp)
print("Waktu kedaluwarsa token:", exp_datetime)
