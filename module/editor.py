import re
import uuid
import requests
import random
import string
import time




def generateImage(prompt,token,style_id='8897ddfe-2f22-4f96-927f-a2589a6d9098'):
    result = requests.post(
                'https://txt2img.res.lightricks.com/txt2img/v1/api/generate',
                params={'prompt':prompt,'style_id':style_id,'priority':'true','high_quality':'true','is_subscriber':'true'},
                headers={'Host': 'txt2img.res.lightricks.com', 'authorization': 'Bearer '+token, 'x-lightricks-auth-token': token, 'x-app-id': 'com.lightricks.pixaloop', 'x-build-number': '1412', 'x-platform': 'android', 'content-length': '0', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'}
            ).json()
    try:
        return result['result_url']
    except:
        return result['error']
def generateImagev2(prompt):
    ids='8-'+str(uuid.uuid4())
    data = {
    'seedValue':'null',
     'inputText':prompt, 
      'width':'512',
      'height':'512', 
      'styleId':'0',
      'styleLabel':'Photo General 1',
      'isPrivate':'true',
      'price':'0',
      'requestId':ids,
      'resultUrl':'https://hotpotmedia.s3.us-east-2.amazonaws.com/'+ids+'.png'
    }
    
    headers = {
      'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
      'Content-Type': "application/multipart-formdata",
      'sec-ch-ua': "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
      'Api-Token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MTA3NDIzOTUsImV4cCI6MTcxMDgyODc5NX0.LL2vEbQiPaJ8g2lKQdgIFpkl_HCiM4GBO4nZnkSd3bw",
      'sec-ch-ua-mobile': "?0",
      'Authorization': "hotpot-t2mJbCr8292aQzp8CnEPaK",
      'sec-ch-ua-platform': "\"Linux\"",
      'Origin': "https://hotpot.ai",
      'Sec-Fetch-Site': "same-site",
      'Sec-Fetch-Mode': "cors",
      'Sec-Fetch-Dest': "empty",
      'Referer': "https://hotpot.ai/",
      'Accept-Language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,su;q=0.6"
    }
    response = requests.post("https://api.hotpot.ai/art-maker-sdte-zmjbcrr", data=data, headers=headers)
    try:
        return eval(response.text)
    except Exception as e:return str(e)
    
def getToken(v=1,email = "".join([random.choice(string.ascii_lowercase) for x in range(10)])):
    email += '@1secmail.com'
    try:
        if v == 1:
            app = "com.lightricks.Enlight-Phoenix"
        elif v == 2:
            app = "com.lightricks.Enlight-Video"
        headers = {'Host': 'api.fortress-ww-prd.lightricks.com', 'accept': 'application/json', 'content-type': 'application/json', 'content-length': '58', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'}
        y = requests.post('https://api.fortress-ww-prd.lightricks.com/v2/auth/otp?app='+app+'&cvc=1412&plt=a&pltv=28&env=production',
                json={
                    "identityType": "email",
                    "identity": email
                },
                headers=headers)
        if not "{}" in y.text:
            return
        kode = ""
        limit = 0
        time.sleep(2)
        while limit<10:
            try:
                time.sleep(0.1)
                inbox = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={email.split("@")[0]}&domain={email.split("@")[1]}').json()
                kode = inbox[0]["subject"].split(': ')[1]
                token = requests.post('https://api.fortress-ww-prd.lightricks.com/v2/auth/email/login?app='+app+'&cvc=1412&plt=a&pltv=28&env=production',headers=headers,json={"email":email,"identityProofType":"email","identityProof":kode})
                return token.json()['token']
                break
            except:pass
        raise('error')
    except Exception as e: return {'error':str(e)}

def editImage(prompt,bytesImage,token,userid):
    url = "https://cf.res.lightricks.com/v2/api/ai-gaming/predict-sync"
    headers = {
        "x-request-id": str(uuid.uuid4()),
        "authorization": "Bearer "+token,
        "x-lightricks-auth-token": token,
        "x-app-id": "com.lightricks.videoleap",
        "x-build-number": "1.25.1",
        "x-platform": "android",
        "x-lightricks-subscriber": "true",
        "x-client-user-id": userid,
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.10.0"
    }
    
    data = {"params": '{"prompt": "'+prompt+'"}'}
    files = {"input": bytesImage}
    response = requests.post(url, headers=headers, files=files,data=data)
    return response
    
    
def generate_string():
    prefix = '01HRP'
    remaining_length = 21 - len(prefix)
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=remaining_length))
    return prefix + random_string

def registerV2(token,frsId):
    response1 = requests.request(
        'PUT',
        'https://feed.creators.lightricks.com/api/v1/clients/register',
        headers={'Host': 'feed.creators.lightricks.com', 'x-lightricks-client-version': '1.25.1:2144', 'x-lightricks-client-locale': 'locale=in_ID;timezone=Asia/Jakarta;network_country=ID', 'x-lightricks-client-id': 'android:videoleap:'+frsId,'authorization':'Bearer '+token, 'content-type': 'application/json; charset=UTF-8', 'content-length': '3641', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'},
        json={"app_name":"videoleap","app_version":"1.25.1","installation_id":frsId,"first_installation_id":frsId,"platform":"android","version_code":2144,"app_capabilities":[{"template_type":"videoleap_template","capabilities":["stock.storyblocks","clip","clip.animation","clip.animation.hover","clip.image","clip.gif","clip.chromaKey.color","clip.chromaKey.trainedModel","clip.audio.maintainsPitch","clip.speed.025-4","clip.transition","clip.transition.blending.asset","clip.transition.blending.mask","clip.transition.feature","clip.transition.displacement.roll","clip.transition.displacement.shake","clip.transition.displacement.shake-zoom","clip.transition.displacement.zoom","clip.transition.displacement.bump","clip.transition.displacement.pan","mixer","mixer.animation","mixer.animation.hover","mixer.image","mixer.gif","mixer.chromaKey.color","mixer.chromaKey.trainedModel","mixer.audio.maintainsPitch","mixer.speed.025-4","sticker","sticker.animation","sticker.animation.hover","sticker.image","sticker.gif","sticker.speed.025-4","audio","audio.maintainsPitch","audio.animation.volume","audio.speed.025-4","audio.soundEffect","audio.voiceOver","text","text.shadow","text.animatedLineSpacing","text.animatedGlyphSpacing","text.animation","text.stroke","text.effect.fire","text.effect.neon","text.fonts.revamp.july23","adjust","defocus","defocus.animation","defocus.blurType.directional","defocus.blurType.zoom","defocus.blurType.radial","filters","filters.animation","filters.pack.vivid","filters.pack.sunny","filters.pack.nature2","filters.pack.tealAndOrange","filters.pack.portrait","filters.pack.blackAndWhite2","filters.pack.clear","filters.pack.vhs","filters.pack.film","rgb","rgb.animation","kaleidoscope","kaleidoscope.animation","kaleidoscopeGrid","kaleidoscopeGrid.animation","pixelate","pixelate.animation","prism","prism.animation","scan","shake","shake.animation","filmGrain","filmGrain.animation","offset","rotation.interpolationMethod.linear","clip.aiTransform","clip.aiImageTransformAnime","clip.aiImageTransformSelfies","clip.aiImageTransformGaming","clip.aiImageTransformComics","clip.aiImageTransformCartoons","clip.aiImageTransformCartoons.aug23","clip.aiImageTransformGamingFlowPresets.oct23","clip.aiImageTransformHalloween","clip.aiImageTransformWonka","clip.aiImageTransformAquaman","clip.aiVideoTransformScenes","clip.aiVideoTransformSelfies","clip.aiVideoTransformAnime","clip.aiVideoTransformGaming","clip.aiVideoTransformComics","clip.aiVideoTransformCartoons","clip.aiVideoTransformCartoons.aug23","clip.aiVideoTransformGamingFlowPresets.oct23","clip.aiVideoTransformHalloween","clip.aiVideoTransformWonka","clip.aiVideoTransformAquaman","mixer.aiTransform","mixer.aiImageTransformAnime","mixer.aiImageTransformSelfies","mixer.aiImageTransformGaming","mixer.aiImageTransformComics","mixer.aiImageTransformCartoons","mixer.aiImageTransformCartoons.aug23","mixer.aiImageTransformGamingFlowPresets.oct23","mixer.aiImageTransformHalloween","mixer.aiImageTransformWonka","mixer.aiImageTransformAquaman","mixer.aiVideoTransformScenes","mixer.aiVideoTransformSelfies","mixer.aiVideoTransformAnime","mixer.aiVideoTransformGaming","mixer.aiVideoTransformComics","mixer.aiVideoTransformCartoons","mixer.aiVideoTransformCartoons.aug23","mixer.aiVideoTransformGamingFlowPresets.oct23","mixer.aiVideoTransformHalloween","mixer.aiVideoTransformWonka","mixer.aiVideoTransformAquaman","aiTransform.remoteConfiguration","clip.aiImageTransformGamingFlowPresets","clip.aiVideoTransformGamingFlowPresets","mixer.aiImageTransformGamingFlowPresets","mixer.aiVideoTransformGamingFlowPresets"]}]}
        )
    return response1.json()

def record():
    frsId = generate_string()
    yy = requests.post('https://analytics-gateway.delta.dp.lightricks.com/record_batch',
    headers={'Host': 'analytics-gateway.delta.dp.lightricks.com', 'ltx-dp-batch-id': frsId, 'ltx-dp-batch-timestamp': str(__import__("time").time())[0:14].replace(".",""), 'content-type': 'avro/binary; schema_id=103055', 'content-length': '3434', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'},
    data=generateData()
    )
    return yy.json()
    
def generateData():
    byte_data = b'\x10\xcc\xdb\x0cHff3babc7-3b46-49bf-a4e0-c34add579eb0\x86\xb9\x8d\xd5\xc5c\x0eandroid\x12videoleap\xf2\x040com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\x86\xb9\x8d\xd5\xc5c\x00Hff3babc7-3b46-49bf-a4e0-c34add579eb0\x02401HRPN379Y4C4A0PDN25YJ72TS\x02\x00\x00\x00\x00\x00\x00\x00\x00401HRPN379Y4C4A0PDN25YJ72TS\x00\x18app_launcher\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\x94\xe5\x0cHa52c65d6-45dc-497b-92b6-c9f0668c1e71\xe2\xd4\x8e\xd5\xc5c\x0eandroid\x12videoleap\xf4\x07\x02Hb5aa7882-499e-437f-b64d-e3e477c81bd60com.lightricks.videoleap\x02\x04en"videoleap_android\x082144\x02\x0c1.25.1\x02B1710157309912-4786807260783716190\x00\x02\x04IDHc685ab6f-6947-423c-b334-d99d68ac13b2\x00\x02\x0esamsung\x02\x10SM-J330G\x00\xe2\xd4\x8e\xd5\xc5c\x00Ha52c65d6-45dc-497b-92b6-c9f0668c1e71\x00\x00\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00\x1c@\x02\x12Mali-T720\x02\x06ARM\x00\x02\x02\xe6\xeb\x89\xd5\xc5c401HRPN379Y4C4A0PDN25YJ72TS\x02&com.android.vending\x02\x01\x00\x02\xe6\xeb\x89\xd5\xc5c\x00\x02\x04ID\x00\x02\x063.1\x028\x02\x029\x0eandroid\x02 c596b93ca298e0ac\x00\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\x00\x00\x02\x18Asia/Jakarta\x02\x00\x02\x04in\x00\xc4\xe7\x0cH07f44c79-e6b1-4b2a-8cf5-7d6c8fe14272\x94\xd5\x8e\xd5\xc5c\x0eandroid\x12videoleap\xc0\x05H9b090a1b-59a9-42cc-9b2a-dcd29728cbde\x1aintro_v_1_2_4\x020com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\x94\xd5\x8e\xd5\xc5c\x00H07f44c79-e6b1-4b2a-8cf5-7d6c8fe14272\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00\x1c@401HRPN379Y4C4A0PDN25YJ72TS\x00\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\xc8\xdb\x0cH52873092-9c39-4643-87f6-9bfc6a6827d4\xb2\xd5\x8e\xd5\xc5c\x0eandroid\x12videoleap\xd8\x040com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\xb2\xd5\x8e\xd5\xc5c\x00H52873092-9c39-4643-87f6-9bfc6a6827d4\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00\x1c@401HRPN379Y4C4A0PDN25YJ72TS\x00\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\xcc\xdb\x0cH2ab3df6b-1cc5-41f5-85b1-5782488b3eeb\xbc\xd5\x8e\xd5\xc5c\x0eandroid\x12videoleap\xf2\x040com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\xbc\xd5\x8e\xd5\xc5c\x00H2ab3df6b-1cc5-41f5-85b1-5782488b3eeb\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00\x1c@401HRPN379Y4C4A0PDN25YJ72TS\x00\x18app_launcher\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\xbc\xe7\x0cHf497cf09-f069-4183-8fe7-170bf1818222\xf4\xd5\x8e\xd5\xc5c\x0eandroid\x12videoleap\xe2\x05H9b090a1b-59a9-42cc-9b2a-dcd29728cbde\x00\x00:start_creating_button_pressed0com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\xf4\xd5\x8e\xd5\xc5c\x00Hf497cf09-f069-4183-8fe7-170bf1818222\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00\x1c@401HRPN379Y4C4A0PDN25YJ72TS\x00\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\xce\xe7\x0cH0d4a6bc3-d80e-4157-a0bd-bc049d273943\x80\xd6\x8e\xd5\xc5c\x0eandroid\x12videoleap\xc8\x05Hd7762593-4304-4ce4-a918-3ac3ccc72952\x06\x02\x1eintro_dismissed\x000com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\x80\xd6\x8e\xd5\xc5c\x00H0d4a6bc3-d80e-4157-a0bd-bc049d273943\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00\x1c@401HRPN379Y4C4A0PDN25YJ72TS\x00\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\xcc\xe7\x0cHe1330d31-4562-4b41-b4d2-1f927194e5c8\xf6\xf4\x8e\xd5\xc5c\x0eandroid\x12videoleap\x96\x06\x02\x02Hd7762593-4304-4ce4-a918-3ac3ccc72952\x00\x00\x00\x00\x00\x00\x10@\x00\x028So, what brings you here? v2\x02\x1eI\xe2\x80\x99m a creator0com.lightricks.videoleap"videoleap_android\x082144Hc685ab6f-6947-423c-b334-d99d68ac13b2\xf6\xf4\x8e\xd5\xc5c\x00He1330d31-4562-4b41-b4d2-1f927194e5c8\x02401HRPN379Y4C4A0PDN25YJ72TS\x04\x00\x00\x00\x00\x00\x00"@401HRPN379Y4C4A0PDN25YJ72TS\x00\x00\x00\x0eandroid\x02 c596b93ca298e0ac\x00\x00H28430bf3-5c17-4363-ad42-f7cd9306e00a\x02H64b683fa-3372-40c7-88a7-0a956be562c5\x00\x00'
    def replace_uuid(match):
        return str(uuid.uuid4())
    
    pattern = re.compile(r'[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12}')
    
    new_data = eval(pattern.sub(replace_uuid, str(byte_data)))
    return new_data
def editVideo(prompt,token,bytesVidio):
    clnId = generate_string()
    reqId = str(uuid.uuid4())
    formt = requests.post('https://cf.res.lightricks.com/v2/api/upload-location',
        headers={'Host': 'cf.res.lightricks.com', 'authorization': 'Bearer '+token, 'x-lightricks-auth-token': token, 'x-app-id': 'com.lightricks.videoleap', 'x-build-number': '1.25.1', 'x-platform': 'android', 'x-lightricks-subscriber': 'true', 'x-client-user-id': clnId, 'content-type': 'application/json; charset=utf-8', 'content-length': '41', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'},
        json={"input_type":"mp4","input_method":"PUT"}).json()
    requests.request(
        'PUT',
        formt['upload_url'],
        headers={'Host': 'storage.googleapis.com', 'x-request-id': reqId, 'authorization': 'Bearer '+token, 'x-lightricks-auth-token': token, 'x-app-id': 'com.lightricks.videoleap', 'x-build-number': '1.25.1', 'x-platform': 'android', 'x-lightricks-subscriber': 'true', 'x-client-user-id': clnId, 'content-type': 'video/mp4', 'content-length': str(len(bytesVidio)), 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'},
        data=bytesVidio)
    predict = requests.post(
            'https://cf.res.lightricks.com/v2/api/vid2vid/predict',
            headers={'Host': 'cf.res.lightricks.com', 'x-request-id': reqId, 'authorization': 'Bearer '+token, 'x-lightricks-auth-token': token, 'x-app-id': 'com.lightricks.videoleap', 'x-build-number': '1.25.1', 'x-platform': 'android', 'x-lightricks-subscriber': 'true', 'x-client-user-id': clnId, 'content-type': 'application/json; charset=utf-8', 'content-length': '903', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.10.0'},
            json={"input_ids": {"input_video": formt['upload_url'].split('?')[0]},"params": {"cn_params": {"preset": "selfiead001","prompt": prompt,"encrypted_preset":"g"},"propagation_type":"NONE","cn_indice_select_mode":"equidistant"}})
    status = predict.json()['status_url']
    return status
    # while True:
    #     time.sleep(5)
    #     try:
    #         progres = requests.get(status).json()
    #         if progres['status-code'] == 'done':
    #             result = progres['results'][0]
    #             return result
    #             break
    #         elif progres['status-code'] == 'in-progress':
    #             print(progres['progress'])
    #             continue
    #         else:
    #             print(progres)
    #             break
    #     except:break
# print(getToken(v=2,email='jfjrjrjrjrjr'))
#print(editVideo('snow, light, night',getToken(v=2,email='jfjdjdjj'),open('/storage/emulated/0/DCIM/Camera/232e82666493a9b96bbad258a5fcbdb0.mp4','rb').read()))