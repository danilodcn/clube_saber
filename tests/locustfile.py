from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    @task
    def bilingue_page(self):
        self.client.get('/admin')
