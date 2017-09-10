# -*- coding:utf-8 -*-  
__author__ = 'chenz'
__date__ = '2017/9/8 21:21'

#抓取v2ex网站标题，作者，链接，并写入csv文件

import requests
import lxml.html
import csv
url = 'https://www.v2ex.com/'
html = requests.get(url).text

doc = lxml.html.fromstring(html)
title = doc.xpath("//span[@class='item_title']/a/text()")
subject = doc.xpath("//span[@class='small fade']/a[@class='node']/text()")
author = doc.xpath("//span[@class='small fade']/strong[1]/a/text()")
link = doc.xpath("//span[@class='item_title']/a/@href")
result = []
for i in range(len(title)):
    dic = {
        'title':title[i],'subject':subject[i],'author':author[i],'link':'https://www.v2ex.com'+str(link[i])
    }
    result.append(dic)
print(result)
headers = ['title','subject','author','link']

with open('f:\\result.csv','w') as f:
    f_csv = csv.DictWriter(f,headers)
    f_csv.writeheader()
    f_csv.writerows(result)

print('ok')


















