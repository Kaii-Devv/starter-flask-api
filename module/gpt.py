import requests
import uuid
class AI:
    def __init__(self,prompt,session=False,cookie=False,chatbotId="eb36b773-8c12-45d6-b6c2-ddffedef5210"):
        ses = requests.Session()
        if not cookie:
            cookie = "_ga=GA1.1.375721201.1705895601;__stripe_mid=6e202ef4-b864-4aba-91d0-801f1eac5baaf162b1;__Host-next-auth.csrf-token=9140508a3dedf7f832bb615b9e9ebcad6fdf9ace1d6186935ee7e605bcb27a56%7C0a0f17b6846ec38cdcf119a0ebb898316b60835eda2fe571686e6bfd32cc28b4;cf_clearance=Yjb4e279qQkLpbl8p7m8QcOnuFIkxwSJgzgD8D2q0Eo-1705914406-1-AUdF8hS1uVp9qxq8m/mIuCvuDcFygbpFCM6zIKaJ2e7PmqNWDlnYdBBYIjn2IyF8EVgYI9A1vaJzhBMS5wnTq8M=;__stripe_sid=5f38cf52-7226-4a48-97e5-da87f4b57b58a9282c;__Secure-next-auth.callback-url=https%3A%2F%2Fora.ai%2Fpricing;ora-api.token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1NTc3MWNmNC0yZGJhLTQyZDYtOTRhMy00ZDU4N2YzNDExOWEiLCJpYXQiOjE3MDU5MTQ0NzEsImV4cCI6MTcwNTkxNDU0Nn0.HAHJFd3xk0D6oOd-X8ROfYWrkNDDjTpy30Qmerq6FnI;__Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..3yyy0QCENGEg0bdH.sJTLyPePymML12AQlQZQpRmcEu5vKwfRRemzzgyvtlEfXPpjcIktVA6mHCv3fTjOhqtzTLb2zdpdvt3Nzts8enLsnkPRgEZ5Y20xuZ2I9de1UY8kb91T8bP2a6H9hU1QSVqTUflPoQ4beS4qGYnHYYnzswh5sAcM__JTDYgvz3D45qBmDtgz-NhZaFqWKgoHSw1azE-pEumjM5gcqBXcOMkQX4SXzaPGO71YQnZ4D-H1MBmiwp4IZAn4WB2XNZ7AVNI_EAQcvASCMd15GFICxshLM_VgkKYDlXRK504Iv-Xzh6W4INlBDG85b6WxE6KNNXAO77rquR62KzWQnZ3aLgkIyJMCx2PzHyJ5pJ4W8DsGGMeA-hUTS_U_1koJnAWnaMpkJaR9HL4pUVkizM3AUbKNheQcdGB6sToZpIsH0eljdzD9sjn5wqO6qjirbV1XRtEa7d8xmKXUaqpVF6lr3a1I4Cu7s1iXdFnbW6vJsd2hTDCItAqsa9KRDXaEoB12EsIE6mtoCjq5IwVSmIU-4SmhSxzVG4iKYHVU4uU9TRnrSFuHCPvJGbcUuuFCbBAoVxGVKtU9HzJiLLtaBvsrR9AI3BQffTS3ZVydfgoPEAZ9xXpJQUnfIwplUh1WmBgEaMri2Q4vkDf-r3vk5HWyxcxp-7Azu3-eqPmqbJ4EYxk7FcM.MC5uwMRJqCAlqW0XH_HZ9Q;_ga_MWL7THFH58=GS1.1.1705914407.3.1.1705914472.0.0.0"
        ses.cookies.update({"cookie":cookie})
        token = ses.get("https://ora.ai/api/auth/session")
        cace = ses.options(f"https://api.ora.ai/users/"+token.json()["user"]["id"]+"/conversation?chatbotId="+chatbotId+"&limit=20")
        data = {"chatbotId":chatbotId,"input":prompt,"userId":token.json()["user"]["id"],"provider":"OPEN_AI","config":{"n":1,"stop":[],"topP":1,"model":"gpt-3.5-turbo","bestOf":1,"stream":False,"maxTokens":1000,"temperature":0.65,"presencePenalty":0,"frequencyPenalty":0},"includeHistory":True}
        if session:
            data.update({"conversationId":session})
        head = {'Host': 'api.ora.ai', 'content-length': '386', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'content-type': 'application/json', 'sec-ch-ua-mobile': '?1', 'authorization': 'Bearer '+token.cookies.get_dict()['ora-api.token'], 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36', 'sec-ch-ua-platform': '"Android"', 'accept': '*/*', 'origin': 'https://ora.ai', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://ora.ai/', 'accept-encoding': '', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6'}
        response = ses.post("https://api.ora.ai/conversations",json=data,headers=head).json()
        try:
            self.session = response["conversationId"]
        except:self.session = "none"
        try:
            self.text = response["response"]["text"]
            self.cookie = ";".join([ f"{key}={value}" for key, value in token.cookies.get_dict().items()])
        except Exception as e: print(response,data)

def send_otp(email):
    ses = requests.Session()
    ses.get(f"https://ora.ai/api/user?email={email}").json()
    verifi = ses.get("https://ora.ai/api/auth/csrf").json()
    data ={
'callbackUrl':'https://ora.ai/signin',
'email':email,
'csrfToken':verifi['csrfToken'],
'json':True}
    send = ses.post("https://ora.ai/api/auth/signin/email?",headers={'Host': 'ora.ai', 'content-length': '155', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'sec-ch-ua-platform': '"Android"', 'sec-ch-ua-mobile': '?1', 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded', 'accept': '*/*', 'origin': 'https://ora.ai', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://ora.ai/signin', 'accept-encoding': '', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6'},data=data)


def generateBot(name,cookie):
    ses = requests.Session()
    if not cookie:
        cookie = "_ga=GA1.1.375721201.1705895601;__stripe_mid=6e202ef4-b864-4aba-91d0-801f1eac5baaf162b1;__Host-next-auth.csrf-token=9140508a3dedf7f832bb615b9e9ebcad6fdf9ace1d6186935ee7e605bcb27a56%7C0a0f17b6846ec38cdcf119a0ebb898316b60835eda2fe571686e6bfd32cc28b4;cf_clearance=Yjb4e279qQkLpbl8p7m8QcOnuFIkxwSJgzgD8D2q0Eo-1705914406-1-AUdF8hS1uVp9qxq8m/mIuCvuDcFygbpFCM6zIKaJ2e7PmqNWDlnYdBBYIjn2IyF8EVgYI9A1vaJzhBMS5wnTq8M=;__stripe_sid=5f38cf52-7226-4a48-97e5-da87f4b57b58a9282c;__Secure-next-auth.callback-url=https%3A%2F%2Fora.ai%2Fpricing;ora-api.token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1NTc3MWNmNC0yZGJhLTQyZDYtOTRhMy00ZDU4N2YzNDExOWEiLCJpYXQiOjE3MDU5MTQ0NzEsImV4cCI6MTcwNTkxNDU0Nn0.HAHJFd3xk0D6oOd-X8ROfYWrkNDDjTpy30Qmerq6FnI;__Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..3yyy0QCENGEg0bdH.sJTLyPePymML12AQlQZQpRmcEu5vKwfRRemzzgyvtlEfXPpjcIktVA6mHCv3fTjOhqtzTLb2zdpdvt3Nzts8enLsnkPRgEZ5Y20xuZ2I9de1UY8kb91T8bP2a6H9hU1QSVqTUflPoQ4beS4qGYnHYYnzswh5sAcM__JTDYgvz3D45qBmDtgz-NhZaFqWKgoHSw1azE-pEumjM5gcqBXcOMkQX4SXzaPGO71YQnZ4D-H1MBmiwp4IZAn4WB2XNZ7AVNI_EAQcvASCMd15GFICxshLM_VgkKYDlXRK504Iv-Xzh6W4INlBDG85b6WxE6KNNXAO77rquR62KzWQnZ3aLgkIyJMCx2PzHyJ5pJ4W8DsGGMeA-hUTS_U_1koJnAWnaMpkJaR9HL4pUVkizM3AUbKNheQcdGB6sToZpIsH0eljdzD9sjn5wqO6qjirbV1XRtEa7d8xmKXUaqpVF6lr3a1I4Cu7s1iXdFnbW6vJsd2hTDCItAqsa9KRDXaEoB12EsIE6mtoCjq5IwVSmIU-4SmhSxzVG4iKYHVU4uU9TRnrSFuHCPvJGbcUuuFCbBAoVxGVKtU9HzJiLLtaBvsrR9AI3BQffTS3ZVydfgoPEAZ9xXpJQUnfIwplUh1WmBgEaMri2Q4vkDf-r3vk5HWyxcxp-7Azu3-eqPmqbJ4EYxk7FcM.MC5uwMRJqCAlqW0XH_HZ9Q;_ga_MWL7THFH58=GS1.1.1705914407.3.1.1705914472.0.0.0"
    ses.cookies.update({"cookie":cookie})
    token = ses.get("https://ora.ai/api/auth/session")
    tokens = token.json()["user"]["id"]
    response = ses.post(
        'https://api.ora.ai/chatbots',
        headers={
            'host': 'api.ora.ai',
            'content-length': '198',
            'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'content-type': 'application/json',
            'sec-ch-ua-mobile':' ?1',
            'authorization': 'Bearer '+tokens,
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua-platform': "Android",
            'accept': '*/*',
            'origin': 'https://ora.ai',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://ora.ai/',
            'accept-encoding': '',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6',},
        json={"prompt":prompt,"userId":str(uuid.uuid4()),"name":"yooo","emoji":"🤝","description":"hdhdhdbbbbb","isService":True,"category":"CAREERS","defaultBotMessage":"hshdhdhsh"}

    )
    