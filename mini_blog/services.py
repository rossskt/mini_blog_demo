from .models import User

def total_posts_by_user(user: User) -> int:
    # BUG #2: user.posts can be None
    return len(user.posts)