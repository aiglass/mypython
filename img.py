#! /usr/local/bin/python3
import requests as rq
import os
url="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573152703975&di=2f5893e7c58200cb6957fb9e57406ba3&imgtype=0&src=http%3A%2F%2Fnewsingeneral.com%2Fwp-content%2Fuploads%2F2013%2F10%2Fapple_gray_logo.png"
#path="/Volumes/MyCode/workspace/python/a.png"
path=url.split('/')[-1]
try:
    if not os.path.exists(path):
        r=rq.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")
