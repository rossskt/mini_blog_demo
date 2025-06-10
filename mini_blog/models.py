from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Post:
    slug: str
    title: str
    body: str
    author: str

@dataclass
class Article:
    # Duplicate of Post for the refactor mission
    slug: str
    headline: str
    content: str
    author: str

@dataclass
class User:
    username: str
    email: str
    posts: Optional[List[Post]] = field(default_factory=list)