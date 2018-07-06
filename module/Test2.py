# coding=utf-8
# create by toonew at 2018/7/6
from requests import get

# 使用from导入,import 选择部分模块

res = get("http://www.baidu.com")
print(res.content)
