#! /usr/local/bin/python3
import requests as rq
url=input('请输入链接: ')
try:
    rs=rq.get(url)
    rs.raise_for_status()
    rs.encoding=rs.apparent_encoding
    print('''
    ===================
    %s
    ==================
    '''%rs.text[:1000])
    print(rs.url)
except:
    print("爬取失败")
