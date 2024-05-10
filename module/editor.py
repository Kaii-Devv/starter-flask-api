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

def find_nearest_divisible_by_eight(n):
    # Fungsi ini mencari bilangan terdekat yang habis dibagi 8
    return 8 * round(n/8)

def get_size(aspect_ratio_string):
    # Set default
    width = 1024
    height = 1024

    # Get aspect ratio

    if aspect_ratio_string != '1:1':
        aspect_ratio_array = aspect_ratio_string.split(':')
        aspect_ratio = int(aspect_ratio_array[0]) / int(aspect_ratio_array[1])

        # Adjust base size for 1:4 and 4:1 aspect ratios. Use @aspect_ratio_string, not @aspect_ratio, to avoid precision errors.
        short_size = 512 if aspect_ratio_string in ['4:1', '1:4'] else 512

        # Use landscape?
        if aspect_ratio > 1:
            height = short_size
            width = find_nearest_divisible_by_eight(round(short_size * aspect_ratio))

        # Nope, set to portrait.
        else:
            width = short_size
            height = find_nearest_divisible_by_eight(round(width / aspect_ratio))

    max_size = max(width, height)

    return {
        'width': width,
        'height': height,
        'max': max_size
    }

def generateImagev2(prompt,style='0',size='1:1'):
    ids=str(uuid.uuid4())
    label = {"0":"Custom","1":"Sketch General 1","10":"Comic Book 1","100":"3D Portrait 1","101":"Product Concept Art 1","102":"Line Art 2","103":"Illustration Art 1","104":"Illustration Art 2","105":"Cute Art 1","107":"Portrait Anime 1","108":"Portrait Anime 2","109":"Portrait Anime 3","11":"Comic Book 2","110":"Portrait Anime 4","113":"Portrait Game 4","114":"Photo Fashion 1","115":"Portrait Gothic 2","116":"Logo Illustration 1","117":"Psychedelic 1","118":"Illustration General 4","119":"Icon Minimal 1","12":"Comic Book 3","120":"Icon Black White 2","121":"Icon 3D 1","122":"Icon Cute 1","123":"Illustration General 2","124":"Isometric 1","125":"Isometric 2","126":"Concept Art 6","127":"Illustration General 5","128":"Concept Art 5","129":"Portrait Game 5","13":"Doom 1","130":"Illustration Art 3","131":"Portrait 6","132":"Portrait 5","133":"Portrait Game  6","134":"Portrait Anime 5","135":"Portrait 4","136":"Portrait 8","137":"Portrait 9","138":"Portrait 10","139":"Hotpot Art 8","14":"Doom 2","140":"Hotpot Art 9","141":"Portrait Concept Art 1","142":"Portrait Concept Art 2","143":"Portrait Game 7","144":"Portrait Concept Art 3","145":"Hotpot Art 10","146":"Concept Art 7","147":"Oil Painting 2","148":"Cyberpunk 1","149":"Cyberpunk 2","15":"Watercolor 1","150":"Chinese Art 1","151":"Chinese Art 2","152":"Chinese Art 3","153":"Japanese Art 2","154":"Photo Moody 1","155":"Watercolor 2","156":"Watercolor 3","158":"Anime Cute 1","159":"Fractal Pattern 1","16":"Japanese Art","160":"Painting Fusion 1","161":"Photo Cinematic 1","162":"Painting Fusion 3","163":"Sculpture Glass 1","164":"Photo Dystopian 1","165":"Painting Black White 1","166":"Painting Fusion 4","167":"Painting Fusion 5","168":"Painting Geometric 1","169":"Illustration Palette 1","17":"Acrylic Art","170":"Watercolor Black White 1","171":"Photo Dystopian 2","172":"Poster War Zone 1","173":"Animation 5","174":"Portrait Anime 6","175":"Portrait Anime 7","178":"Hotpot Art 11","179":"Hotpot Art 12","18":"Graffiti","180":"Photo General 2","181":"Hotpot Ephemeral Wisp 1","182":"Game Art 1","183":"Comic Book 6","184":"Bacon Art 1","185":"Anime Fantasy 1","186":"Anime 2","187":"Anime 3","188":"Portrait Anime 8","189":"Anime 4","19":"Hotpot Art 1","190":"Anime Realistic 1","191":"Anime 5","192":"Anime Van Gogh 1","193":"Photo Black White 1","194":"Photo Cinematic 2","195":"Demon Black White 1","196":"Iridescent Marble 1","197":"Photo Fashion 2","198":"Logo Minimal 1","199":"Anime 6","20":"Hotpot Art 2","200":"Doom 3","201":"Fast Blur 1","202":"Bioluminescence 1","203":"Iridescent Metal 1","204":"3D Toy 1","205":"Pizza Art 1","206":"Halftone Dystopian 1 ","207":"Cyberorganic 1","21":"Hotpot Art 3","22":"Hotpot Art 5","24":"Pixel Art","25":"Sculpture General 1","26":"Fantasy 1","27":"Fantasy 2","28":"Fantasy 3","29":"Anime 1","3":"Sketch General 3","30":"Anime Black White","31":"Anime Berserk","32":"Anime Korean 1","33":"Portrait 1","34":"Portrait 2","35":"Portrait 3","36":"Portrait Mugshot","37":"Portrait Marble","38":"Portrait Gothic","39":"Oil Painting 1","4":"Sketch Scribble Black White 1","40":"3D Black White","41":"3D General 1","42":"3D Print 1","43":"3D General 2","44":"3D General 3","45":"3D Voxel 1","46":"3D Minecraft 1","47":"3D Roblox 1","48":"Photo General Volumetric Lighting 1","49":"Photo General 1","5":"Sketch Scribble Color 1","53":"Illustration General 1","54":"Charcoal 1","55":"Charcoal 2","56":"Charcoal 3","57":"Steampunk","58":"Line Art","59":"Gothic","6":"Icon Black White","60":"Animation 1","61":"Animation 2","62":"Architecture Interior Modern 1","63":"Architecture General 1","64":"Sci-fi 1","65":"Logo Detailed 1","66":"Logo Draft 1","67":"Logo Clean 1","68":"Logo Hipster 1","69":"Illustration Flat","7":"Icon Flat","70":"Animation 3","71":"Concept Art 2","72":"Cartoon 1","73":"Comic Book 4","74":"Architecture Interior 1","75":"Architecture Exterior 1","76":"Comic Book 5","77":"Concept Art 3","78":"Stained Glass 1","79":"Animation 4","8":"Icon Sticker Black White","80":"Retro Art","81":"Pop Art","82":"Illustration Smooth","83":"Portrait Game 1","84":"Concept Art 4","85":"Sci-fi 2","86":"Sci-fi 3","87":"Logo Sticker 1","88":"Painting Huang Gongwang 1","89":"Painting Claude Monet 1","9":"Icon Sticker","90":"Painting Pablo Picasso 1","91":"Painting Paul Cezanne 1","92":"Painting Salvador Dali 1","93":"Painting Vincent Van Gogh 1","95":"Portrait Figurine 1","96":"Low Poly 1","97":"Low Poly 2","98":"Portrait Game 2","99":"Portrait Game 3"}
    data = {'seedValue':'null','inputText':prompt, 'width':'512','max':'512','height':'512', 'styleId':style,'styleLabel':label[style],'isPrivate':'true','price':'0','requestId':ids,'resultUrl':'https://hotpotmedia.s3.us-east-2.amazonaws.com/'+ids+'.png'}
    data.update(get_size(size))
    #print(data)
    headers = {
      'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
      #'Content-Type': "application/multipart-formdata",
      'sec-ch-ua': "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
      'Api-Token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MTA3NzE4MDQsImV4cCI6MTc0MTkzOTk1M30.HTJNdJgCMhOwP08NRIan_qI3AbRWz33MqnALrU2RdU8",
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
    response = requests.post("https://api.hotpot.ai/art-premium-test1", data=data, headers=headers)
    try:
        return eval(response.text)
    except Exception as e:print(e);print(response.text);raise(e)

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