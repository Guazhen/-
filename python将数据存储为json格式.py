# coding:utf-8

#导入json模块
import json
#导入BeautifulSoup模块
from bs4 import BeautifulSoup
import requests
#构造浏览器头信息
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User_Agent':user_agent}

r = requests.get('http://seputu.com/',headers=headers)
soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
content=[]

#find_all查找class_ = "mulu"
for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
    #如果找到了mulu
    if h2 != None:
        #去字符串的值
        h2_title = h2.string
        list = []
        #在mulu标签中查找mulu href
        for a in mulu.find(class_='box').find_all('a'):
            href = a.get('href')
            box_title = a.get('title')
            #将href,title添加到list列表中
            list.append({'href':href,'box_title':box_title})
        #将文件内容加入到content
        content.append({'title':h2_title,'content':list})

with open('qiye.json','wb') as fp:
    #json的dump方法将content写入到qiye.txt文件中
    json.dump(content,fp=fp,indent=4)
