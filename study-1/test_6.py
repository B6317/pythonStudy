# coding=utf-8
# create by toonew at 2018/1/29

from __future__ import print_function

f = open('./test_4.txt')


def find(str1, query):
    dic = {}
    words = str1.split()
    for word in words:
        dic.setdefault(word, 0)
        dic[word] += 1
    return dic[query]


print(find(f.read(), 'and'))
