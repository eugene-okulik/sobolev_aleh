from locust import HttpUser, task, between
import random


class BlogUser(HttpUser):
    wait_time = between(1, 2)

    @task(3)
    def get_all_posts(self):
        self.client.get("/posts")

    @task(2)
    def get_post_by_id(self):
        post_id = random.choice([1, 2, 3])
        self.client.get(f"/posts/{post_id}")

    @task(1)
    def get_comments_for_post(self):
        post_id = random.choice([1, 2, 3])
        self.client.get(f"/comments?postId={post_id}")

    @task(1)
    def create_post(self):
        payload = {
            "title": "foot",
            "body": "bar",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        self.client.post("/posts", json=payload, headers=headers)

    @task(1)
    def update_post(self):
        post_id = random.randint(1, 3)
        payload = {
            "id": post_id,
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        headers = {'Content-Type': 'application/json'}
        self.client.put(f"/posts/{post_id}", json=payload, headers=headers)

    @task(1)
    def patch_post(self):
        post_id = random.randint(1, 3)
        payload = {
            "title": "foo",
            "body": "asd"
        }
        headers = {'Content-Type': 'application/json'}
        self.client.patch(f"/posts/{post_id}", json=payload, headers=headers)
