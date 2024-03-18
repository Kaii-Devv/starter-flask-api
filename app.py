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
        Body=json.dumps(data),
        Bucket="cyclic-cautious-pear-cod-eu-west-2",
        Key=key
    )
def getData(key="database.json"):
    my_file = s3.get_object(
        Bucket="cyclic-cautious-pear-cod-eu-west-2",
        Key=key
    )
    return json.loads(my_file['Body'].read())

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

upData({'gpt': {'cookies':''}})
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
    if prompt:
        try:
            result = generateImagev2(prompt.replace("+"," "))
            upData(requests.get(result,stream=True).content,key=result.split('/')[-1])
            return {'result':'succes','patch':'/content/'+result.split('/')[-1]}
        except Exception:return {'error':str(e)}
    else:
        return {"error":str(prompt)}

@app.route('/content/<patch>')
def konten(patch):
    return send_file(getData(key=patch), mimetype='image/jpeg')

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
    return getData()['gpt']['cookies']
@app.route("/api/gpt3")
def gpt3():
    sesi = request.args.get("session")
    prompt = request.args.get("prompt")
    cookie = getData()['gpt']['cookies']
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
        upData({'gpt':{'cookies':cookie}})
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
    

