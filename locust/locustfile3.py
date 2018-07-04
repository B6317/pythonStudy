# coding=utf-8
# create by toonew at 2018/7/5
# 代码出处： http://www.moye.me/2017/06/24/locust-load-testing/
from __future__ import print_function
from locust import HttpLocust, TaskSet, task
from hashlib import sha1
import time
import uuid
import hmac
import json

secret = "__HOLY_SECRET_KEY__"
username = "Luke"
password = "I'mYourFather"
host = "http://example.org"
loginUrl = "/api/users/login"
apiUrl = "/api/dummy/test"


def hmacsha1(plaintext, secret):
    return hmac.new(secret, plaintext, sha1).hexdigest()


def timestamp():
    return str(int(time.time()))


def nonce():
    return str(uuid.uuid1())


def auth_header():
    ts = timestamp()
    nc = nonce()
    checksum = hmacsha1(ts + nc, secret)
    return {"Content-type": "application/json",
            "timestamp": ts,
            "nonce": nc,
            "checksum": checksum}


class MyTaskSet(TaskSet):
    def on_start(self):
        self.tokenInfo = None
        headers = auth_header()
        data = json.dumps({"username": username, "password": password})
        response = self.client.request(method="POST", url=loginUrl,
                                       data=data,
                                       headers=headers)
        print("LOGIN RESULT:", response.status_code, response.content)
        if response.status_code == 200:
            self.tokenInfo = json.loads(response.content)

    @task
    def dummy_test(self):
        if self.tokenInfo is not None:
            token = self.tokenInfo["token"]
            headers = auth_header()
            headers["Authorization"] = "Bearer " + token
            response = self.client.request(method="GET", url=apiUrl,
                                           headers=headers)
            print("API RESULT:", response.status_code, response.content)


class MyLocust(HttpLocust):
    task_set = MyTaskSet
    host = host
