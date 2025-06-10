import pytest
from mini_blog.services import total_posts_by_user
from mini_blog.models import User

def test_total_posts_none():
    user = User(username="kim", email="kim@example.com", posts=None)
    with pytest.raises(TypeError):
        total_posts_by_user(user)