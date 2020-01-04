import requests as rq
url="http://m.ip138.com/ip.asp?ip="
r=rq.get(url+'182.150.160.251')
print(r.text[-500:])
