import pytest
import requests

from resources.data import DataTest

class TestJSONPlaceholder:

    BASE_URL = DataTest.JSON_PLACEHOLDER_BASE_URL

    def test_get_posts(self, responses):
        data = responses["json_placeholder"]["posts"].json()
        assert isinstance(data, list), "Posts should be a list"

    @pytest.mark.parametrize("user_id", [1, 5, 10])
    def test_get_posts_by_user(self, user_id):
        response = DataTest.get_response(f"{self.BASE_URL}/posts", params={"userId": user_id})
        data = response.json()
        assert all(post["userId"] == user_id for post in data), "User ID mismatch in posts"

    def test_create_post(self):
        payload = {"title": "foo", "body": "bar", "userId": 1}
        response = requests.post(f"{self.BASE_URL}/posts", json=payload)
        assert response.ok, f"Failed to create a post with status code {response.status_code}"
        data = response.json()
        assert data["title"] == "foo" and data["body"] == "bar" and data["userId"] == 1, "Post creation response mismatch"

    def test_get_comments(self, responses):
        data = responses["json_placeholder"]["comments"].json()
        assert isinstance(data, list), "Comments should be a list"

    @pytest.mark.parametrize("post_id", [1, 5, 10])
    def test_get_comments_by_post(self, post_id):
        response = DataTest.get_response(f"{self.BASE_URL}/comments", params={"postId": post_id})
        data = response.json()
        assert all(comment["postId"] == post_id for comment in data), "Post ID mismatch in comments"

    def test_delete_post(self):
        post_id = 1
        response = requests.delete(f"{self.BASE_URL}/posts/{post_id}")
        assert response.ok, f"Failed to delete post with status code {response.status_code}"
        # Проверяем, что повторное получение удаленного поста возвращает ошибку или пустой результат
        get_response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
        assert get_response.status_code == 404, "Post was not properly deleted"