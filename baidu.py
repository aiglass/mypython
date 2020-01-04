#! /usr/local/bin/python
import requests as rq
key=input('请输入关键词:  ')
kv= {'wd':key}
r=rq.get('http://www.baidu.com/s',params=kv)
print(r.status_code)
print(r.url)
print(len(r.text))
