#! /usr/local/bin/python3
import re
#re.search()搜索字符串内第一个匹配正则表达式的位置
match=re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))
#re.match()从字符串的开始位置起匹配正则表达式
match2=re.match(r'[1-9]\d{5}','100081')
if match2:
    print(match2.group(0))
#re.findall()搜索字符串中所有匹配的子串并以列表类型返回
match3=re.findall(r'[1-9]\d{5}','100082 100001 100111')
list=[]
if match3:
    print(match3)
#re.split()对结果进行分割
match4=re.split(r'[1-9]\d{5}','bit100082 tsu100001 tsu100111',maxsplit=1)
if match4:
    print(match4)
#re.finditer()
for m in re.finditer(r'[1-9]\d{5}','bit100011 tes100033 tau 100081'):
    if m:
        print(m.group(0))
#re.sub()替换
match5=re.sub(r'[1-9]\d{5}',':zipcode','bit100011 tes100033 tau100081')
print(match5)
