# coding=utf-8
# create by toonew at 2018/7/4
# 运行命令：locust -f locustfile1.py --host=http://localhost:8080
from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/login", {"username": "ellen_key", "password": "education"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 200
    max_wait = 500
