from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from database.session import SessionLocal
from core.security import decode_access_token
from repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    email = payload.get("sub")

    if not email:
        raise HTTPException(
            status_code=401,
            detail="Invalid token payload"
        )

    user = UserRepository.get_by_email(
        db,
        email
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user
