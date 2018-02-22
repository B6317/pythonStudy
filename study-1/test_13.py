# coding=utf-8
# create by toonew at 2018/2/22
import requests
from pyquery import PyQuery as pq

r = requests.get('http://tieba.baidu.com/p/2166231880', auth=('user', 'pass'))

d = pq(r.text)

imgs = d.find('.BDE_Image')

x = 0
for img in imgs.items():
    print(img.attr('src'))
    x += 1
    with open('./test/{0}.jpg'.format(x), "wb") as file:
        imgRequest = requests.get(img.attr('src'))
        file.write(imgRequest.content)
