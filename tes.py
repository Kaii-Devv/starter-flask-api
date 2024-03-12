import os

def encpass(pw,tamp):
    pw = bytearray(pw.encode('utf-8'))
    byter = bytearray(os.urandom(32))
    tamp = bytearray(tamp.encode('utf-8'))
    