
from flask import Flask
import os
from module.bingai import get_images
from module.proxi import filterProxy
from module.gpt import AI
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os,subprocess
import random,time
import threading
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED
app = Flask(__name__)
@app.route('/')
def hello_world():
    return send_file("index.html")

@app.route('/api/proxy')
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
@app.route("/api/uptime")
def uptime():
    target = request.args.get("target")
    if not target:return {'error':str(target)}
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
    else:return {"error":str(prompt)}

@app.route("/api/gpt3")
def gpt3():
    prompt = request.args.get("prompt").split("+"," ")
    respon = AI(prompt)
    return {"response":respon.text,"session":respon.session}