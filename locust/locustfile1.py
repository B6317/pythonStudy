# coding=utf-8
# create by toonew at 2018/7/4
from locust import HttpLocust, TaskSet


def login(l):
    l.client.post("/login", {"username": "ellen_key", "password": "education"})


def index(l):
    l.client.get("/")


def profile(l):
    l.client.get("/profile")


class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}  # 大佬 大佬，python这json，index直接是变量对应的值 措手不及。。

    def on_start(self):
        login(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
