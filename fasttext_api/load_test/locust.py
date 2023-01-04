from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)

    @task
    def on_start(self):
        self.client.get("/")

    @task
    def predict(self):
        self.client.post("/predict")