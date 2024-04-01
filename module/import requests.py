import requests

url = 'https://cutechat.editapp.ai/api/claim_reward'
headers = {
    'host': 'cutechat.editapp.ai',
    'content-length': '0',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'content-type': 'application/json',
    'sec-ch-ua-mobile': '?0',
    'authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImJhNjI1OTZmNTJmNTJlZDQ0MDQ5Mzk2YmU3ZGYzNGQyYzY0ZjQ1M2UiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiQklTS0lNQSIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NLcTFMN09MSEZLQlN0Z1FubzBUeFJoMWFONC1SVFB5VGhhRF9aX0o0US09czk2LWMiLCJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY3V0ZWNoYXQtMWQwNWYiLCJhdWQiOiJjdXRlY2hhdC0xZDA1ZiIsImF1dGhfdGltZSI6MTcxMTY5MjgyNiwidXNlcl9pZCI6IktHV0NYSTVka1dWdXhrTDB1R0ZFbFVrQWNhejEiLCJzdWIiOiJLR1dDWEk1ZGtXVnV4a0wwdUdGRWxVa0FjYXoxIiwiaWF0IjoxNzExNjkyODI2LCJleHAiOjE3MTE2OTY0MjYsImVtYWlsIjoiY2VtaWxhbmlubkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJnb29nbGUuY29tIjpbIjExMTUzNTc2NjIxODg0NTI2NDc3MyJdLCJlbWFpbCI6WyJjZW1pbGFuaW5uQGdtYWlsLmNvbSJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.C__3D3UFsU_NSVFGjCDKOe9Gn32omuk8pzNkA4oZizY2k_G75sukD8uRZas28eVXKbX2_QtKdNWxY0z9fpU4FrVWu3LmX-OecqO-AbvxZQEDdB0ie1xG_PHbxYf-B6tOgjp3bqysfI029p2yH5LAa-WTFu_6n769pShxr65-cntiYv9luQPHNInA6kSD3z7dQXM2BiyOeFAudeKUd-7TcGa1zvj8g7InITsB47aei8qKmNUpg8aeMZVYobsTmP7JZce9DpLMJPof5ApUbpDQCZidUb5DdyDnVtb1evoA63GhOMe1bxujT9v6zvF_ctlJirqmZ0quKBktfN_XJppAGg',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Android"',
    'accept': '*/*',
    'origin': 'https://cutechat.ai',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://cutechat.ai/',
    'accept-encoding': 'gzip, deflate, br, zstd',
    #'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
}

response = requests.post(url, headers=headers)

print(response.text)
