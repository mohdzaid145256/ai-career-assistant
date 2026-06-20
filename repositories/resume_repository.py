from sqlalchemy.orm import Session

from models.resume import Resume


class ResumeRepository:

    @staticmethod
    def create(
        db: Session,
        user_id: int,
        file_name: str,
        file_path: str,
        file_size: int
    ):
        resume = Resume(
            user_id=user_id,
            file_name=file_name,
            file_path=file_path,
            file_size=file_size
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        return resume

    @staticmethod
    def get_by_user_id(
        db: Session,
        user_id: int
    ):
        return (
            db.query(Resume)
            .filter(Resume.user_id == user_id)
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        resume_id: int
    ):
        return (
            db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    @staticmethod
    def delete(
        db: Session,
        resume: Resume
    ):
        db.delete(resume)
        db.commit()
