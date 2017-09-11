# -*- coding:utf-8 -*-  
__author__ = 'chenz'
__date__ = '2017/9/10 14:31'
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common import by
import lxml.html
import time,os,csv


chromedriver = 'E:\chromedriver\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#打开一点资讯网页
driver.get('https://www.yidianzixun.com/')
#因为这个网页不是响应式的，所以先最大化，才能加载出旁边的刷新按钮
driver.maximize_window()
#等待3秒
driver.implicitly_wait(3)
#根据class找到刷新按钮，点击刷新按钮，获取最新资讯
driver.find_element_by_css_selector(".item.refresh.icon.iconfont.icon-refresh.anim").click()
#执行多次页面下拉脚本
for i in range(0,6):
    driver.execute_script("window.scrollBy(0,200)","")
    time.sleep(3)

doc = lxml.html.fromstring(driver.page_source)
#文章标题
title = doc.xpath("""//a[@class='item doc style-small-image style-content-middle']
          /div[@class='doc-content']/div[@class='doc-content-inline']
          /div[@class='doc-title']/text()""")
#作者
author = doc.xpath("""
//a[@class='item doc style-small-image style-content-middle']
/div[@class='doc-content']/div[@class='doc-content-inline']
/div[@class='doc-info']/span[@class='source']/text()
""")
#评论数
comment = doc.xpath("""
//a[@class='item doc style-small-image style-content-middle']
/div[@class='doc-content']/div[@class='doc-content-inline']
/div[@class='doc-info']/span[@class='comment-count']/text()
""")
#链接
link = doc.xpath("""
//div[@class='main index-main']/div[@class='channel-news channel-news-0']
/a[@class='item doc style-small-image style-content-middle']/@href
""")


result = []
for i in range(len(title)):
    dic = {'title':title[i],'author':author[i],'comment':comment[i],'link':link[i]}
    result.append(dic)

#表头
headers = ['title','author','comment','link']
with open('f:\\yidianzixun.csv','w')  as f:
    f = csv.DictWriter(f,headers)
    f.writeheader()
    f.writerows(result)
print('ok')