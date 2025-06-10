import pytest
from fastapi.testclient import TestClient
from mini_blog.api import app

client = TestClient(app)

def test_create_post_api():
    resp = client.post("/posts", json={
        "slug": "hello",
        "title": "Hello",
        "body": "World",
        "author": "kim"
    })
    assert resp.status_code == 201, resp.text