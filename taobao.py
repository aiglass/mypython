#! /usr/local/bin/python3
import requests as rq
import re

def getHTMLText(url):
    try:
        headers={
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
            "cookie":"miid=282565792026161574; cna=ISgHE9RyXSICAd9XzSRv6EQk; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; tg=0; enc=VrobrSsV%2FyPCeNX6O%2FTGVyImB3WiKcg3NB9ek6SeM%2BHcn%2FNrBb20EkO%2BSSzsIgD34KVVnQICeUNDOpd%2FBE%2Bbxw%3D%3D; t=f2be6da5377dc883a3bcc8310099e6b8; UM_distinctid=16cad3d544f462-0dfdb66bb90198-38637706-1fa400-16cad3d54501ac; tracknick=wd18140014935; _cc_=V32FPkk%2Fhw%3D%3D; v=0; cookie2=6141fa358f973864175fd69e2404b692; _tb_token_=e336eb739631; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; JSESSIONID=04C853105657D19B59EAEFB50E1B5BD9; l=dBN0NquRv_Vc2x5sBOCaPurza7yFSIRYmuPzaNbMi_5d86L_HD_OkQwDTFp6VSWfT0TB4onLKn29-etXsdy06Pt-g3fPaxDc.; isg=BDMz58bRah_nbyc9KEa2AIMUwjGdwMVPnLA3juXQj9KJ5FOGbThXepF-nlSuwB8i"
        }
        r=rq.get(url,headers=headers)
        r.raise_for_status()
        return r.text
    except:
        return ""

def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        return ""

def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))

def main():
    goods='macbookpro'
    depth=3
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

main()
