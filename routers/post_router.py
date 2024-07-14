from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.schemas import PostCreate
from services.post_service import create_post, get_user_posts, delete_post
from services.auth_service import get_current_user
from utils.database import get_db
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/add-post")
def add_post(
    post: PostCreate, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    current_user = get_current_user(db, token)
    return create_post(db, post, current_user)


@router.get("/get-posts")
def get_user_posts_route(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    current_user = get_current_user(db, token)
    print("current_user: ", current_user)
    return get_user_posts(db, current_user)


@router.delete("/delete-post/{post_id}")
def delete_post_route(
    post_id: int, token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    current_user = get_current_user(db, token)
    return delete_post(db, post_id, current_user)
