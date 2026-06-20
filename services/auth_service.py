from sqlalchemy.orm import Session

from core.security import (
    hash_password,
    verify_password
)

from repositories.user_repository import UserRepository
from schemas.auth import UserRegister


class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        user_data: UserRegister
    ):
        existing_user = UserRepository.get_by_email(
            db,
            user_data.email
        )

        if existing_user:
            raise ValueError(
                "Email already registered"
            )

        hashed_password = hash_password(
            user_data.password
        )

        return UserRepository.create(
            db=db,
            full_name=user_data.full_name,
            email=user_data.email,
            hashed_password=hashed_password
        )

    @staticmethod
    def authenticate_user(
        db: Session,
        email: str,
        password: str
    ):
        user = UserRepository.get_by_email(
            db,
            email
        )

        if not user:
            return None

        if not verify_password(
            password,
            user.hashed_password
        ):
            return None

        return user
