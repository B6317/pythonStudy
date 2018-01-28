# coding=utf-8
# create by toonew at 2018/1/28
import random
import string


def active_code(count, length):  # 激活码生成
    base = string.uppercase + string.lowercase + string.digits  # 生成激活码可能包含的字符集
    return [''.join(random.sample(base, length)) for i in range(count)]


if __name__ == "__main__":
    print active_code(10, 16)
