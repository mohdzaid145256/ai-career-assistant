from sqlalchemy.orm import Session

from repositories.parsed_resume_repository import (
    ParsedResumeRepository
)


class ParsedResumeService:

    @staticmethod
    def create_parsed_resume(
        db: Session,
        resume_id: int,
        raw_text: str
    ):
        return ParsedResumeRepository.create(
            db=db,
            resume_id=resume_id,
            raw_text=raw_text
        )

    @staticmethod
    def get_by_resume_id(
        db: Session,
        resume_id: int
    ):
        return ParsedResumeRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )
