from sqlalchemy.orm import Session

from repositories.resume_repository import ResumeRepository


class ResumeService:

    @staticmethod
    def create_resume(
        db: Session,
        user_id: int,
        file_name: str,
        file_path: str,
        file_size: int
    ):
        return ResumeRepository.create(
            db=db,
            user_id=user_id,
            file_name=file_name,
            file_path=file_path,
            file_size=file_size
        )

    @staticmethod
    def get_user_resumes(
        db: Session,
        user_id: int
    ):
        return ResumeRepository.get_by_user_id(
            db,
            user_id
        )

    @staticmethod
    def get_resume(
        db: Session,
        resume_id: int
    ):
        return ResumeRepository.get_by_id(
            db,
            resume_id
        )

    @staticmethod
    def delete_resume(
        db: Session,
        resume
    ):
        ResumeRepository.delete(
            db,
            resume
        )
