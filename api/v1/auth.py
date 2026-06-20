from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.dependencies import (
    get_db,
    get_current_user
)

from schemas.auth import (
    UserRegister,
    UserLogin
)

from services.auth_service import AuthService
from core.security import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    user_data: UserRegister,
    db: Session = Depends(get_db)
):
    try:
        user = AuthService.register_user(
            db,
            user_data
        )

        return {
            "message": "User registered successfully",
            "user_id": user.id,
            "email": user.email
        }

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):
    user = AuthService.authenticate_user(
        db,
        user_data.email,
        user_data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "created_at": current_user.created_at
    }
