#! /usr/local/bin/python3
import requests as rq
from bs4 import BeautifulSoup as bs
import bs4
import re

#获取大学排名网网页内容getHtmlText()
def getHtmlText(url):
    try:
        rs=rq.get(url,timeout=30)
        rs.raise_for_status()
        rs.encoding=rs.apparent_encoding
        return rs.text
    except:
        return "爬取失败!"

#提取网页内容中的数据并存储到适合的数据结构fillUnivList()
def fillUnivList(ulist,html):
    soup=bs(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[3].string])
    pass

#利用数据结构展示并输出结果printUnivList(ulist,num)
def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

def main():
    ulist=[]
    url='http://www.zuihaodaxue.com/Greater_China_Ranking2018_0.html'
    html=getHtmlText(url)
    fillUnivList(ulist,html)
    num=input('please in num:  ')
    printUnivList(ulist,int(num))

main()
