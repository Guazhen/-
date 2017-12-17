#! /usr/bin/env python   
# -*- coding: utf-8 -*- 

import csv
from lxml import etree
import re
import requests

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User_Agent':user_agent}
r = requests.get('http://seputu.com/',headers = headers)

#lxml解析html
html = etree.HTML(r.text)
#提取
div_mulus = html.xpath('.//*[@class="mulu"]')
pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
rows = []
for div_mulu in div_mulus:
    #提取文本内容
    div_h2 = div_mulu.xpath('./div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        h2_title = div_h2[0].encode('utf-8')
        #提取连接
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath('./@href')[0]
            box_title = a.xpath('./@title')[0]
            pattern = re.compile(r'\s*\[(.*)\]\s+(.*)')
            match = pattern.search(box_title)
            if match != None:
                date = match.group(1).encode('utf-8')
                real_title = match.group(2).encode('utf-8')
                content = (h2_title,real_title,href,date)
                print content
                rows.append(content)
headers = ['title','real_title','href','date']
with open('qiye.csv','w') as f:
    #返回writer对象f_csv
    f_csv = csv.writer(f)
    #对句柄f_csv操作，写一行
    f_csv.writerow(headers)
    #写入多行
    f_csv.writerows(rows)

