import requests
class AI:
    def __init__(self,prompt,session=False,cookie=False):
        ses = requests.Session()
        if not cookie:
            try:
                cookie = open(".cookies.txt","r").read()
            except:
                cookie = "_ga=GA1.1.375721201.1705895601;__stripe_mid=6e202ef4-b864-4aba-91d0-801f1eac5baaf162b1;__stripe_sid=2ca8cdca-5001-410b-a24e-46bef9fc0d67688be5;__Host-next-auth.csrf-token=67d7a33532d9d61ee36aa8dc48bf8d4272c53d2a0c326d51932de16b2293886b%7Cb45e6ae5ad5087daae0dc5ed6cae204f5700f22834a23849f9cbfcdeff158708;__Secure-next-auth.callback-url=https%3A%2F%2Fora.ai;cf_clearance=GTuzw4btNjYIBiy43B3VBdemx8eDadhKuxZCmIiFmMs-1705898242-1-AeruqQI3i5/Jr0FtXGviETgulwH5oMeJ4l66+gTJM2dUngRJaZ/pwQaE07p33ACjkvHPPASqCOrJooLyUweSbJc=;ora-api.token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1NTc3MWNmNC0yZGJhLTQyZDYtOTRhMy00ZDU4N2YzNDExOWEiLCJpYXQiOjE3MDU4OTk1OTcsImV4cCI6MTcwNTg5OTY3Mn0.OIbB953L4MRBclyhNFv7BOLITOVDRB7ufcImzxfLIv4;__Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..0HzGt_HttAR28bM6.4Vi0lIxI_A6aGc0-Q5SQjBiIS0juiahg5pzKntf1ZycrAcfR1jEC9siHBrkVM0Lw_gkDckOOnY89BJ5vsjmRFG-LRN6QbCB6RB213pTQVDhMBNj_EIlVpArbFn0OmeEdwexC2VJMdbs6cud3MbKUvWEJGzC9Ffd4WOKfo7mz6MDTbcAPgaFYeDiJiB_3bFiyXAVnygB3tacelAeRP7OQj8Yn7n-OnqQUvc6_9DujEWz06S0ksnnxw0r9gsid2OXQCuplkwVP4vWjHUO1aLQKzh3648pRxuFlKBm34NFMxt-JBCUIEqTcQESRmPBInOuaQG20gHhODtuDwb0J_t5JW2O_W7wpyGjSdmiWCtqsW2QAgexPfquMcdT6ilTnDjf3N4LqOOpgAy_dvqCpJ8g_UO1b05H6tL3YsXJN9I6d987SlXWX8IkF79ogm6SfiHP1xofde-gmtQzDtLlGuiXvQYaP6sAH0raXCTzwKF1Y6BUGiDsmN5cMFh2gCGrM3pJbJxUjentjeePPFbYwB7BhKvwmDXfw8BOpviLpyfTL236CwUKS0sAkVM6oMpnZVfMvhGi6arxzokrkUfAzXQydKoOVNDYd-SW_VvvaFCRaD4-HqLRyqEcpSX14Ji-kRd_1y_zopaEPIlI7KXRpy7c5lnTJcpDw-fBobA9BaZnDQ0AM1RM.WpO4UeOPr7QDTHcfqSM9Vg;_ga_MWL7THFH58=GS1.1.1705895601.1.1.1705899597.0.0.0"
        ses.cookies.update({"cookie":cookie})
        token = ses.get("https://ora.ai/api/auth/session")
        ses.options(f"https://api.ora.ai/users/"+token.json()["user"]["id"]+"/conversation?chatbotId=eb36b773-8c12-45d6-b6c2-ddffedef5210&limit=20")
        data = {"chatbotId":"eb36b773-8c12-45d6-b6c2-ddffedef5210","input":prompt,"userId":token.json()["user"]["id"],"provider":"OPEN_AI","config":{"n":1,"stop":[],"topP":1,"model":"gpt-3.5-turbo","bestOf":1,"stream":False,"maxTokens":1000,"temperature":0.65,"presencePenalty":0,"frequencyPenalty":0},"includeHistory":True}
        if session:
            data.update({"conversationId":session})
        head = {'Host': 'api.ora.ai', 'content-length': '386', 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"', 'content-type': 'application/json', 'sec-ch-ua-mobile': '?1', 'authorization': 'Bearer '+token.cookies.get_dict()['ora-api.token'], 'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36', 'sec-ch-ua-platform': '"Android"', 'accept': '*/*', 'origin': 'https://ora.ai', 'sec-fetch-site': 'same-site', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 'referer': 'https://ora.ai/', 'accept-encoding': '', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6'}
        response = ses.post("https://api.ora.ai/conversations",json=data,headers=head).json()
        self.session = response["conversationId"]
        self.text = response["response"]["text"]
        self.cookie = ";".join([ f"{key}={value}" for key, value in ses.cookies.get_dict().items()])
        open(".cookies.txt","w").write(self.cookie)