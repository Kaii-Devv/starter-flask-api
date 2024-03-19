# Muhamad Idris
from module.bingai import get_images
from module.proxi import filterProxy
from module.gpt import AI, send_otp
from module.gmails import email
from module.editor import generateImage, getToken, editImage, editVideo, generateImagev2
import boto3
import json
from module.dump import number, random_number
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests
import re
import os
import subprocess
import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED
email_pass =     "qosjjhwdzdmscfmm"
my_email   = "cemilaninn@gmail.com"
s3 = boto3.client('s3')
#exit(dir(s3))
app = Flask(__name__)
@app.route('/')
def hello_world():
    return send_file("index.html")
def upData(data,key="database.json"):
    s3.put_object(
        Body=data,
        Bucket="cyclic-cautious-pear-cod-eu-west-2",
        Key=key
    )
def getData(key="database.json"):
    my_file = s3.get_object(
        Bucket="cyclic-cautious-pear-cod-eu-west-2",
        Key=key
    )
    return my_file['Body'].read()

def get_s3_object_url(object_key):
    """
    Mengambil URL dari objek di Amazon S3.
    Args:
        bucket_name (str): Nama bucket di Amazon S3.
        object_key (str): Kunci objek (nama file) di dalam bucket.
    Returns:
        str: URL dari objek di Amazon S3.
    """
    try:
        url = s3.download_file("get_object", Params={"Bucket": "cyclic-cautious-pear-cod-eu-west-2", "Key": object_key}, ExpiresIn=3600)
        return url
    except Exception as e:
        print(f"Error: {e}")
        return None

upData(json.dumps({'gpt': {'cookies':''}}))
@app.route('/api/proxy')
def proxy():
    try:
        types = request.args.get('type')
    except:
        types = False
    valid = []
    if not types:
        types = 'socks5'
    proxylist = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype='+types+'&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
    with ThreadPoolExecutor(max_workers=int(len(proxylist))+2) as pool:
        for proxy in proxylist:
            pool.submit(filterProxy,types+'://'+proxy,valid)
    return {'author':'Muhammad Idris','result':valid}

@app.route('/content/all_image_result.json')
def all():
    response = s3.list_objects_v2(Bucket="cyclic-cautious-pear-cod-eu-west-2",FetchOwner=False)
    res = [obj['key'] if obj for obj in response["Contents"]]
    return res

@app.route("/api/uptime")
def uptime():
    target = request.args.get("target")
    if not target:
        target = "https://nfd2st-33517.csb.app"
    upprox = proxy()["result"]
    while True:
        proxyp = random.choice(upprox)
        if len(upprox)<2:break
        try:
            return requests.get(target,proxies=proxyp,timeout=3).text
            break
        except Exception as e:
            upprox.remove(proxyp)
    return {"error":upprox}

@app.route("/api/imagegen")
def imagegenv2():
    prompt = request.args.get("prompt")
    token = request.args.get("token")
    if prompt:
        return generateImage(prompt.replace("+"," "),token)
    else:
        return {"error":str(prompt)}

@app.route("/api/imagegenv2")
def imagegen():
    prompt = request.args.get("prompt")
    styleId = request.args.get('style')
    if not styleId:
        styleId = '0'
    if prompt:
        try:
            result = generateImagev2(prompt.replace("+"," "),style=styleId)
            upData(requests.get(result,stream=True).content,key=result.split('/')[-1])
            return {'author':'Muhamad Idris','result':'succes','patch':'/content/'+result.split('/')[-1]}
        except Exception as e:return {'error':str(e)}
    else:
        return {"error":str(prompt)}
@app.route("/api/imagegenv2/style.json")
def st():
    return {'0': 'Custom', '1': 'Sketch General 1', '3': 'Sketch General 3', '4': 'Sketch Scribble Black White 1', '5': 'Sketch Scribble Color 1', '6': 'Icon Black White', '7': 'Icon Flat', '8': 'Icon Sticker Black White', '9': 'Icon Sticker', '10': 'Comic Book 1', '11': 'Comic Book 2', '12': 'Comic Book 3', '13': 'Doom 1', '14': 'Doom 2', '15': 'Watercolor 1', '16': 'Japanese Art', '17': 'Acrylic Art', '18': 'Graffiti', '19': 'Hotpot Art 1', '20': 'Hotpot Art 2', '21': 'Hotpot Art 3', '22': 'Hotpot Art 5', '24': 'Pixel Art', '25': 'Sculpture General 1', '26': 'Fantasy 1', '27': 'Fantasy 2', '28': 'Fantasy 3', '29': 'Anime 1', '30': 'Anime Black White', '31': 'Anime Berserk', '32': 'Anime Korean 1', '33': 'Portrait 1', '34': 'Portrait 2', '35': 'Portrait 3', '36': 'Portrait Mugshot', '37': 'Portrait Marble', '38': 'Portrait Gothic', '39': 'Oil Painting 1', '40': '3D Black White', '41': '3D General 1', '42': '3D Print 1', '43': '3D General 2', '44': '3D General 3', '45': '3D Voxel 1', '46': '3D Minecraft 1', '47': '3D Roblox 1', '48': 'Photo General Volumetric Lighting 1', '49': 'Photo General 1', '53': 'Illustration General 1', '54': 'Charcoal 1', '55': 'Charcoal 2', '56': 'Charcoal 3', '57': 'Steampunk', '58': 'Line Art', '59': 'Gothic', '60': 'Animation 1', '61': 'Animation 2', '62': 'Architecture Interior Modern 1', '63': 'Architecture General 1', '64': 'Sci-fi 1', '65': 'Logo Detailed 1', '66': 'Logo Draft 1', '67': 'Logo Clean 1', '68': 'Logo Hipster 1', '69': 'Illustration Flat', '70': 'Animation 3', '71': 'Concept Art 2', '72': 'Cartoon 1', '73': 'Comic Book 4', '74': 'Architecture Interior 1', '75': 'Architecture Exterior 1', '76': 'Comic Book 5', '77': 'Concept Art 3', '78': 'Stained Glass 1', '79': 'Animation 4', '80': 'Retro Art', '81': 'Pop Art', '82': 'Illustration Smooth', '83': 'Portrait Game 1', '84': 'Concept Art 4', '85': 'Sci-fi 2', '86': 'Sci-fi 3', '87': 'Logo Sticker 1', '88': 'Painting Huang Gongwang 1', '89': 'Painting Claude Monet 1', '90': 'Painting Pablo Picasso 1', '91': 'Painting Paul Cezanne 1', '92': 'Painting Salvador Dali 1', '93': 'Painting Vincent Van Gogh 1', '95': 'Portrait Figurine 1', '96': 'Low Poly 1', '97': 'Low Poly 2', '98': 'Portrait Game 2', '99': 'Portrait Game 3', '100': '3D Portrait 1', '101': 'Product Concept Art 1', '102': 'Line Art 2', '103': 'Illustration Art 1', '104': 'Illustration Art 2', '105': 'Cute Art 1', '107': 'Portrait Anime 1', '108': 'Portrait Anime 2', '109': 'Portrait Anime 3', '110': 'Portrait Anime 4', '113': 'Portrait Game 4', '114': 'Photo Fashion 1', '115': 'Portrait Gothic 2', '116': 'Logo Illustration 1', '117': 'Psychedelic 1', '118': 'Illustration General 4', '119': 'Icon Minimal 1', '120': 'Icon Black White 2', '121': 'Icon 3D 1', '122': 'Icon Cute 1', '123': 'Illustration General 2', '124': 'Isometric 1', '125': 'Isometric 2', '126': 'Concept Art 6', '127': 'Illustration General 5', '128': 'Concept Art 5', '129': 'Portrait Game 5', '130': 'Illustration Art 3', '131': 'Portrait 6', '132': 'Portrait 5', '133': 'Portrait Game  6', '134': 'Portrait Anime 5', '135': 'Portrait 4', '136': 'Portrait 8', '137': 'Portrait 9', '138': 'Portrait 10', '139': 'Hotpot Art 8', '140': 'Hotpot Art 9', '141': 'Portrait Concept Art 1', '142': 'Portrait Concept Art 2', '143': 'Portrait Game 7', '144': 'Portrait Concept Art 3', '145': 'Hotpot Art 10', '146': 'Concept Art 7', '147': 'Oil Painting 2', '148': 'Cyberpunk 1', '149': 'Cyberpunk 2', '150': 'Chinese Art 1', '151': 'Chinese Art 2', '152': 'Chinese Art 3', '153': 'Japanese Art 2', '154': 'Photo Moody 1', '155': 'Watercolor 2', '156': 'Watercolor 3', '158': 'Anime Cute 1', '159': 'Fractal Pattern 1', '160': 'Painting Fusion 1', '161': 'Photo Cinematic 1', '162': 'Painting Fusion 3', '163': 'Sculpture Glass 1', '164': 'Photo Dystopian 1', '165': 'Painting Black White 1', '166': 'Painting Fusion 4', '167': 'Painting Fusion 5', '168': 'Painting Geometric 1', '169': 'Illustration Palette 1', '170': 'Watercolor Black White 1', '171': 'Photo Dystopian 2', '172': 'Poster War Zone 1', '173': 'Animation 5', '174': 'Portrait Anime 6', '175': 'Portrait Anime 7', '178': 'Hotpot Art 11', '179': 'Hotpot Art 12', '180': 'Photo General 2', '181': 'Hotpot Ephemeral Wisp 1', '182': 'Game Art 1', '183': 'Comic Book 6', '184': 'Bacon Art 1', '185': 'Anime Fantasy 1', '186': 'Anime 2', '187': 'Anime 3', '188': 'Portrait Anime 8', '189': 'Anime 4', '190': 'Anime Realistic 1', '191': 'Anime 5', '192': 'Anime Van Gogh 1', '193': 'Photo Black White 1', '194': 'Photo Cinematic 2', '195': 'Demon Black White 1', '196': 'Iridescent Marble 1', '197': 'Photo Fashion 2', '198': 'Logo Minimal 1', '199': 'Anime 6', '200': 'Doom 3', '201': 'Fast Blur 1', '202': 'Bioluminescence 1', '203': 'Iridescent Metal 1', '204': '3D Toy 1', '205': 'Pizza Art 1', '206': 'Halftone Dystopian 1 ', '207': 'Cyberorganic 1'}
@app.route('/content/<patch>')
def konten(patch):
   # return send_file(getData(key=patch), mimetype='image/jpeg')
    bit = getData(key=patch)
    try:
        return bit , 200, {'Content-Type': 'image/jpeg'}
    except Exception as e:return {type(bit):str(bit)}

@app.route('/api/token')
def toks():
    v = request.args.get('v')
    mail = request.args.get('secmail')
    if v and mail:
        return getToken(v=int(v),email=mail)
    elif v:
        return getToken(v=int(v))
    else:
        return "need params v"
@app.route('/cookies')
def ck():
    return json.loads(getData())['gpt']['cookies']
@app.route("/api/gpt3")
def gpt3():
    sesi = request.args.get("session")
    prompt = request.args.get("prompt")
    cookie = json.loads(getData())['gpt']['cookies']
    try:
        respon = AI(prompt,session=sesi,cookie=cookie)
    except:
        send_otp(my_email)
        time.sleep(2)
        mail = email(my_email,email_pass)
        if mail:
            for cek in mail.msg:
                try:
                    url = re.search('https://(.*?)gmail.com',cek).group(0)
                    ses = requests.Session()
                    ses.get(url).url
                    res = ses.get("https://ora.ai/api/auth/session")
                    cookie = ";".join([ f"{key}={value}" for key, value in res.cookies.get_dict().items()])
                    break
                except Exception as e:pass
        try:
            respon = AI(prompt,session=sesi,cookie=cookie)
        except:
            return {"error":""}
        upData(json.dumps({'gpt':{'cookies':cookie}}))
    try:
        return {'author':'Muhammad Idris',"response":respon.text,"session":respon.session}
    except:
        return "tes"

@app.route('/api/editor/vidio',methods=["POST"])
def genimage():
    data = request.files.get('video')
    token = request.form.get('token')
    prompt = request.form.get('prompt')
    if data and token and prompt:
        byts = data.read()
        return {'progres':editVideo(prompt,token,byts)}
    else:return {'error':'need data'}

@app.route("/api/fb/dump/number")
def dump_number():
    awal = request.args.get("number")
    error = []
    lens = request.args.get("len")
    if not lens or not lens.isdecimal():
        error.append("len")
    trys = request.args.get("try")
    if not trys or not trys.isdecimal():
        error.append("try")
    maxs = request.args.get("max")
    if not maxs or not maxs.isdecimal():
        maxs="50"
    if len(error) != 0:
        err = ", ".join(error)
        return {"error":f"argumen '{err}' not falid"}
    _els = request.args.get("else")
    if _els:
        _els = _els.split(',')
    else:
        _els = []
    
    numbers = list(set(awal + random_number(int(lens) - int(len(awal))) for x in range(int(trys))))

    full=[]
    ses = requests.session()
    res1 = ses.get("https://mbasic.facebook.com/login/identify/")
    inputs = re.findall('<input.*?/>',res1.text)
    with ThreadPoolExecutor(max_workers=len(numbers)/2) as pool:
        for xn in numbers:
            if not xn in _els:
                data = { re.search('name="(.*?)"',x).group(1):re.search('value="(.*?)"',x).group(1) if "value" in x else xn for x in inputs}
                number(full,int(maxs),data,ses)
    return {'author':'Muhammad Idris','result':full}
    
#app.run(debug=True)
    

