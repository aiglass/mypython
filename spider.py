#! /usr/local/bin/python3
import requests as rq
url=input('please input url here:  ')
rp=rq.get(url)
rp.encoding=rp.apparent_encoding
r=rp.text
print ('''
=========================
content:
    %s
=========================
'''%r)
