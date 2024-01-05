from flask import Flask
import os
from flask import Flask, send_file, request, jsonify, render_template, Response
import requests, re, io,os,subprocess
import random,time
import threading
start_time = time.time()
antre =[]
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!<br>Myname Muhamad Idris'
