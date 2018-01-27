# -*- coding=utf-8
# python3.4 爬虫教程
# 倒入文件  （python3  将urllib 和urllib2合并成为一个
import urllib.request

url = "http://www.douban.com/"

# 打开url请求，webPage 为 httpResponse
webPage = urllib.request.urlopen(url)
# 解析httpResponse中的 textView 内容
data = webPage.read()
data = data.decode('UTF-8')

# 输出基本的信息
print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
