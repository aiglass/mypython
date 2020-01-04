#! /usr/local/bin/python3
import re
import requests as rq 
from bs4 import BeautifulSoup
import traceback
import time
#获取url对应的页面
def getHTMLText(url,encoding):
    try:
        r=rq.get(url)
        r.raise_for_status()
        r.encoding=encoding
        return r.text
    except:
        return ""

#获取股票列表
def getStockList(lst,stockUrl):
    html=getHTMLText(stockUrl,'gb2312')
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    count=0
    for i in a:
        # time.sleep(0.01)
        count=count+1
        print('\r当前速度:{:.2f}%'.format(count*100/len(a)),end="")
        try:
            href=i.attrs['href']
            stock=re.findall(r"[s][hz]\d{6}",href)[0]
            lst.append(stock)
        except:
            continue
    

def getStockInfo(lst,stockUrl,fpath):
    for stock in lst:
        url=stockUrl+stock+'.shtml'
        html=getHTMLText(url,'gb2312')
        try:
            if html=="":
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockinfo=soup.find('div','stockInfo')
            name=stockinfo.find('div','name').find_all('h2')[0]
            code=re.findall(r'\d{6}?',stockinfo.find('div','name').find_all('h2')[1].string)[0]
            infoDict.update({'股票名称':name.text})
        except:
            continue

def printStockInfo():
    return ""

def main():
    stock_list_url='http://quote.eastmoney.com/stock_list.html'
    stock_info_url='http://stock.quote.stockstar.com/'
    output_file='stockinfo.txt'
    slist=[]
    getStockList(slist,stock_list_url)
    time.sleep(0.01)
    print('\n完成!')
    print('完成!')
#    print(slist[0])
#    getStockInfo(slist,stock_info_url,output_file)

main()