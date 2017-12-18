# coding:utf-8

import urllib
from lxml import etree
import requests

def Schedule(blocknum,blocksize,totalsize):
    per = 100.0 * blocknum*blocksize / totalsize
    if per > 100:
        per = 100
    print '当前进度:%d' % per

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'
headers = {'User-Agent':user_agent}
r = requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
html = etree.HTML(r.text)
img_urls=html.xpath('.//img/@src')
i = 0
for img_url in img_urls:
  # The hook will be passed three arguments; a count of blocks transferred so far,
  #a block size in bytes, and the total size of the file.
    urllib.urlretrieve(img_url,'img'+str(i)+'.jpg',Schedule)
    i+=1
