from sqlalchemy.orm import Session

from models.parsed_resume import ParsedResume


class ParsedResumeRepository:

    @staticmethod
    def create(
        db: Session,
        resume_id: int,
        raw_text: str
    ):
        parsed_resume = ParsedResume(
            resume_id=resume_id,
            raw_text=raw_text
        )

        db.add(parsed_resume)
        db.commit()
        db.refresh(parsed_resume)

        return parsed_resume

    @staticmethod
    def get_by_resume_id(
        db: Session,
        resume_id: int
    ):
        return (
            db.query(ParsedResume)
            .filter(
                ParsedResume.resume_id == resume_id
            )
            .first()
        )
