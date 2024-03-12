# Muhamad Idris
from module.bingai import get_images
from module.proxi import filterProxy
from module.gpt import AI, send_otp
from module.gmails import email
from module.editor import generateImage, getToken, editImage, editVideo

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
app = Flask(__name__)
@app.route('/')
def hello_world():
    return send_file("index.html")

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
def imagegen():
    prompt = request.args.get("prompt").replace("+"," ")
    if prompt:
        return get_images(prompt)
    else:
        return {"error":str(prompt)}

@app.route("/api/gpt3")
def gpt3():
    sesi = request.args.get("session")
    prompt = request.args.get("prompt")
    cookie = requests.get("https://idristkj2.pythonanywhere.com/cookies").text
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
        requests.get("https://idristkj2.pythonanywhere.com/cookies",params={'cok':cookie})
    try:
        return {'author':'Muhammad Idris',"response":respon.text,"session":respon.session}
    except:
        return "tes"

@app.route('/api/editor/vidio',methods=["POST","GET"])
def genimage():
    data = request.files['video']
    token = request.form['token']
    prompt = request.form['prompt']
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
    

