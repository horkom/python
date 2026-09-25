import os

import requests


class YougileApi:
    BASE_URL = "https://ru.yougile.com/api-v2"

    def __init__(self, token=None):
        self.token = token or os.environ.get("YOUGILE_TOKEN", "")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def create_project(self, title):
        return requests.post(
            f"{self.BASE_URL}/projects",
            headers=self.headers,
            json={"title": title},
        )

    def get_project(self, project_id):
        return requests.get(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
        )

    def update_project(self, project_id, new_title):
        return requests.put(
            f"{self.BASE_URL}/projects/{project_id}",
            headers=self.headers,
            json={"title": new_title},
        )
