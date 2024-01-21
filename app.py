from flask import Flask
import os
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os,subprocess
import random,time
import threading
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello guys!<br>Myname Muhamad Idris<br>API ini full menggunakan flask python'

def filterProxy(proxy,valid):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
                    }
        response = requests.request(
                    'GET',
                    'https://ipinfo.io/json',
                    proxies=proxies,timeout=3
                    )
        if not "ID" in response.json()['country']:
            valid.append(proxies)
    except Exception as e:pass

@app.route('/proxy')
def proxy():
    try:types = request.args.get('type')
    except:types = False
    valid = []
    if not types:
        types = 'socks5'
    proxylist = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype='+types+'&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
    with ThreadPoolExecutor(max_workers=int(len(proxylist))+2) as pool:
        for proxy in proxylist:
            pool.submit(filterProxy,types+'://'+proxy,valid)
    return {'result':valid}
@app.route("/uptime")
def uptime():
    upprox = proxy()["result"]
    while True:
        proxyp = random.choice(upprox)
        if len(upprox)<2:break
        try:
            return requests.get("https://nfd2st-33517.csb.app",proxies=proxyp,timeout=3).json()
            break
        except Exception as e:
            print(e)
            upprox.remove(proxyp)
    return {"error":upprox}


