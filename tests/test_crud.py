import pytest
from mini_blog.crud import create_post, get_post
from mini_blog.models import Post

def test_create_and_get_post():
    post = Post(slug="hello", title="Hello", body="World", author="kim")
    create_post(post)
    retrieved = get_post("hello")
    assert retrieved is post, "Post retrieval failed"