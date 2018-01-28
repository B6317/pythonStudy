# coding=utf-8
# create by toonew at 2018/1/28
import re

import operator

dic = {}
words = []

with open('./test_4.txt') as f:
    line = f.readline()
    while line:
        line = re.sub(r'[.?!,"/]', ' ', line)
        line = re.sub(r' - ', ' ', line)  # 替换单独的‘-’
        words.extend(line.split())  # 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
        # words = words + re.split(',|;|\*|\n|\s', line)
        for word in line.split():
            dic.setdefault(word.lower(), 0)  # 不区分大小写
            dic[word.lower()] += 1
        line = f.readline()

print words
print len(words)
print dic
# items取出键值对，以(x,y)形式，operator.ite（取出指定位置的值），reverse默认倒序
sorted_x = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
print sorted_x

# with 等价于下面，他简化的是关闭这一套。。语法糖 http://blog.csdn.net/suwei19870312/article/details/23258495/
# f2 = open("./test_4.txt")
# try:
#     line = f2.readline()
#     while line:
#         print line
#         line = f2.readline()
# finally:
#     f2.close()
