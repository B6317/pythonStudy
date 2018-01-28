# coding=utf-8
# create by toonew at 2018/1/28
import redis
from test_1 import active_code

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.sadd('active_codes', *set(active_code(200, 16)))
