import random
from locust import HttpUser, task, between

class StressTest(HttpUser):
    wait_time = between(5, 9)

    @task
    def index_page(self):
        self.client.get("/")
