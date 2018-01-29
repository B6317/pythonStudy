# coding=utf-8
# create by toonew at 2018/1/29
from __future__ import print_function

import os

from os.path import join

dic = {"code": 0, "comment": 0, "blank": 0}


# 分析代码文件
def stat_code(f1):
    is_comment = False

    line = f1.readline()
    while line:
        line = line.strip()
        if line != "":
            if not is_comment:
                if line.startswith("'''") or line.startswith('"""'):
                    is_comment = True
                    dic['comment'] += 1
                elif line.startswith("#"):
                    dic['comment'] += 1
                elif line.find('#') > 0:
                    dic['code'] += 1
                    dic['comment'] += 1
                else:
                    dic['code'] += 1
            else:
                if line.endswith("'''") or line.endswith('"""'):
                    is_comment = False
                    dic['comment'] += 1
                else:
                    dic['comment'] += 1
        else:
            dic['blank'] += 1
        line = f1.readline()


if __name__ == "__main__":
    my_path = os.getcwd()
    file_list = [join(my_path, f) for f in os.listdir(my_path) if f.endswith('py')]

    for f in file_list:
        f = open(f)
        stat_code(f)

    print('read file end !!')

    print('###########  result #############')
    print(dic)
    print('###########  result #############')
