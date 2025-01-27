import pytest
import requests

from resources.data import DataTest

class TestJSONPlaceholder:

    BASE_URL = DataTest.JSON_PLACEHOLDER_BASE_URL

    def test_get_posts(self):
        data = DataTest.get_response(f"{self.BASE_URL}/posts")
        assert isinstance(data, list), "Posts should be a list"

    @pytest.mark.parametrize("user_id", [1, 5, 10])
    def test_get_posts_by_user(self, user_id):
        data = DataTest.get_response(f"{self.BASE_URL}/posts", params={"userId": user_id})
        assert all(post["userId"] == user_id for post in data), "User ID mismatch in posts"

    def test_create_post(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        assert response.ok, f"Failed to create a post with status code {response.status_code}"
        data = response.json()
        assert data["title"] == "foo" and data["body"] == "bar" and data["userId"] == 1, "Post creation response mismatch"

    def test_get_comments(self):
        data = DataTest.get_response(f"{self.BASE_URL}/comments")
        assert isinstance(data, list), "Comments should be a list"

    @pytest.mark.parametrize("post_id", [1, 5, 10])
    def test_get_comments_by_post(self, post_id):
        data = DataTest.get_response(f"{self.BASE_URL}/comments", params={"postId": post_id})
        assert all(comment["postId"] == post_id for comment in data), "Post ID mismatch in comments"