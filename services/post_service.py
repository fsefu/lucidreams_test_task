from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from models.models import Post
from schemas.schemas import PostCreate
from utils.database import get_db
from services.auth_service import get_current_user
from models.models import User


def create_post(db: Session, post: PostCreate, user: User):
    db_post = Post(text=post.text, owner_id=user.id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_posts(db: Session, user: User):
    return db.query(Post).filter(Post.owner_id == user.id).all()


def delete_post(db: Session, post_id: int, user: User):
    post = db.query(Post).filter(Post.id == post_id, Post.owner_id == user.id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted"}


def get_user_posts(db: Session, current_user: User):
    posts = db.query(Post).filter(Post.owner_id == current_user.id).all()
    return posts


# def remove_post(db: Session, post_id: int, current_user: User):
#     # Implementation for removing a post
#     pass
