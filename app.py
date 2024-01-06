from flask import Flask
import os
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os,subprocess
import random,time
import threading
from concurrent.futures import ThreadPoolExecutor,as_completed,wait,FIRST_COMPLETED
start_time = time.time()
antre ={}
app = Flask(__name__)
database={}
@app.route('/')
def hello_world():
    return 'Hello, world!<br>Myname Muhamad Idris'
def check(proxy,tok,hasil,pool):
  if len(str(hasil))>5:return
  proxy = {
    'http': 'socks5://'+proxy,
    'https': 'socks5://'+proxy
}
  try:
    ses=requests.Session()
    host= 'https://d0o0d.com'
    ses.proxies.update(proxy)
    log2=ses.get(host+"/e/"+tok,headers={'Host': 'd0o0d.com', 'referer': 'https://d0o0d.com/e/', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/4.9.0'},timeout=3)
    if not 'ddos' in log2.text.lower():
        link=host+"/pass_md5/"+re.search("/pass_md5/(.*?)', function",str(log2.text)).group(1)
        result = ses.get(link,headers={"Host": host.replace('https://',''),"referer": log2.url,"accept-encoding": "gzip","cookie": "lang=1","user-agent": "okhttp/4.9.0"},timeout=3).text+"".join([random.choice('abcdefghijklmnopqrstuvwxyz1234567890') for _ in range(10)])+"?token="+link.split("/")[-1]+"&expiry=1"+"".join([str(random.randrange(1,9)) for _ in range(12)])
        ini = ses.get(result,headers={'Range': 'bytes=0-', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/83.0.144 Chrome/77.0.3865.144 Safari/537.36', 'Referer': 'https://dooood.com/', 'Connection': 'Keep-Alive', 'Accept-Encoding': 'gzip'},stream=True,timeout=3)
        hasil.update({'response':ini,'headers':ini.headers})
        pool.shutdown()
    else:pass
  except Exception as e :pass
@app.route('/d/')
def unduh():
  try:
      tok = request.args.get('token')
      if tok:
          pass
      else:
          return {'return': 'need params token'}

      proxy = requests.get(
          'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
      proxies = proxy.split("\r\n") #np.char.replace(proxy.split('\n')[:-1], '\r', '')
      hasil={}
      file='dood/'+tok+'.mp4'
      with ThreadPoolExecutor(max_workers=20) as pool:
          for proxy in proxies:
              pool.submit(check, proxy, tok,hasil,pool)
      runtime = round(time.time() - start_time,2)
      
      try:
          heads = hasil['headers']
          threading.Thread(target=build,args=(hasil['response'],tok)).start()
          return {'runtimeAPI':runtime,'result':'sending','size':str(hasil['headers']['Content-Length']),'warning':'wait for generate content'}
      except Exception as e:
          if tok in database:
              return {'runtimeAPI':runtime,'result':'succes'}
          elif tok in antre:return {'runtimeAPI':runtime,'result':'generating','size':str(antre[tok])}

  except Exception as e:
      return {'result': str(e)}

def build(ini,tok):
    global database,antre
    achunk=b''
    try:
        
        for chunk in ini.raw.stream(100485, decode_content=False):
            achunk+=chunk
            antre[tok]+=len(chunk)
    except Exception as e:pass
    database.update({tok:io.BytesIO(achunk)})
    achunk=b''
    antre.pop(tok)





@app.route('/v/<tok>')
def unduhv(tok):
  global database,antre
  try:
      try:
         database.pop(tok)
         antre.pop(tok)
      except:pass
      proxy = requests.get(
          'https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=all&ssl=all&anonymity=all').text
      proxies = proxy.split("\r\n") #np.char.replace(proxy.split('\n')[:-1], '\r', '')
      hasil={}
      with ThreadPoolExecutor(max_workers=20) as pool:
          for proxy in proxies:
              pool.submit(check, proxy, tok,hasil,pool)
      runtime = round(time.time() - start_time,2)
#      return Response(hasil['response'].iter_content(chunk_size=18000), content_type='video/mp4')
      return send_file(hasil['response'].raw, mimetype='video/mp4', as_attachment=True, download_name=tok+'.mp4')
  except Exception as e:
      return {'result': str(e)}


def filterProxy(proxy,valid):
    try:
        proxies = {
            'http': proxy,
            'https': proxy
                    }
        response = requests.request(
                    'GET',
                    'https://ipinfo.io/json',
                    proxies=proxies,timeout=5
                    )
        if not "ID" in response.json()['country']:
            valid.append(proxies)
    except Exception as e:pass

@app.route('/proxy')
def proxy():
    types = request.args.get('type')
    valid = []
    if not types:
        types = 'socks5'
    proxylist = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype='+types+'&timeout=10000&country=all&ssl=all&anonymity=all').text.split('\r\n')
    with ThreadPoolExecutor(max_workers=200) as pool:
        for proxy in proxylist:
            pool.submit(filterProxy,types+'://'+proxy,valid)
    return {'result':valid}


@app.route('/e/<judul>')
def read(judul):
    global database,antre
    try:
        if judul in antre:
            return {"warning":'content is loading'}
        elif judul in database:
#            return send_file(database[judul], mimetype='video/mp4', as_attachment=True, download_name=judul+'.mp4')
            return Response(database[judul], content_type='video/mp4')
        else:return {'warning':'video not load'}
    except Exception as e:return {'warning':str(e)}
#print(proxy())