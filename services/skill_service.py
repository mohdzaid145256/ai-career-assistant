from sqlalchemy.orm import Session

from repositories.skill_repository import (
    SkillRepository
)


class SkillService:

    @staticmethod
    def create_skill(
        db: Session,
        resume_id: int,
        skill_name: str
    ):
        return SkillRepository.create(
            db=db,
            resume_id=resume_id,
            skill_name=skill_name
        )

    @staticmethod
    def get_resume_skills(
        db: Session,
        resume_id: int
    ):
        return SkillRepository.get_by_resume_id(
            db=db,
            resume_id=resume_id
        )
