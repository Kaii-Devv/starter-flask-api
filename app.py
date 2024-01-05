from flask import Flask
import os
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os,asyncio,subprocess,speedtest
import random,time
start_time = time.time()
antre =[]
import threading
import numpy as np
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!<br>Myname Muhamad Idris'
