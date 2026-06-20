from sqlalchemy.orm import Session

from models.user import User


class UserRepository:

    @staticmethod
    def get_by_email(
        db: Session,
        email: str
    ):
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        full_name: str,
        email: str,
        hashed_password: str
    ):
        user = User(
            full_name=full_name,
            email=email,
            hashed_password=hashed_password
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
