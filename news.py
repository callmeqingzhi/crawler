# -*- coding:utf-8 -*-  
__author__ = 'chenz'
__date__ = '2017/9/5 21:45'
#爬取凤凰网新闻，并且将爬取结果写入一个txt文件中
import requests
import lxml.html
url = 'http://news.ifeng.com/listpage/11502/0/1/rtlist.shtml'
html = requests.get(url).text
doc = lxml.html.fromstring(html)
title = doc.xpath("//div[@class='newsList']/ul/li/a/text()");
path = doc.xpath("//div[@class='newsList']/ul/li/a/@href");
f = open('news.txt','w',encoding='utf-8')


for i in range(len(title)):
    result = {'标题':title[i],'连接':path[i]}
    print(result)
    f.write(str(result)+'\n')
f.close()