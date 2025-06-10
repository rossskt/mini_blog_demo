from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from .crud import create_post, list_posts
from .models import Post

app = FastAPI()

class PostIn(BaseModel):
    slug: str
    title: str
    body: str
    author: str

@app.post("/posts", response_model=PostIn)
async def create(post_in: PostIn):
    post = Post(**post_in.dict())
    # BUG #3: missing await on async create_post (pretend create_post is sync but treat as async for failure)
    create_post(post)
    return post_in

@app.get("/posts", response_model=List[PostIn])
async def all_posts():
    return list_posts()