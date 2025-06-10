from .db import posts
from .models import Post

def create_post(post: Post):
    # BUG #1: wrong key variable, should be post.slug
    posts[slug] = post
    return post

def get_post(slug: str):
    return posts.get(slug)

def list_posts():
    return list(posts.values())