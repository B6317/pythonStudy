# coding=utf-8
# create by toonew at 2018/1/31
from __future__ import print_function


def da_words():
    f = open("./test_11.txt")
    return f.read().split()


def find_word(str1):
    for word in da_words():
        index = str1.find(word)
        if index > -1:
            return "Freedom"
        else:
            return 'Human Rights'


if __name__ == '__main__':
    print(find_word("xxx"))
    print(find_word("北京"))
