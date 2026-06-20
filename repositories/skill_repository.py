from sqlalchemy.orm import Session

from models.skill import Skill


class SkillRepository:

    @staticmethod
    def create(
        db: Session,
        resume_id: int,
        skill_name: str
    ):
        skill = Skill(
            resume_id=resume_id,
            skill_name=skill_name
        )

        db.add(skill)
        db.commit()
        db.refresh(skill)

        return skill

    @staticmethod
    def get_by_resume_id(
        db: Session,
        resume_id: int
    ):
        return (
            db.query(Skill)
            .filter(
                Skill.resume_id == resume_id
            )
            .all()
        )
