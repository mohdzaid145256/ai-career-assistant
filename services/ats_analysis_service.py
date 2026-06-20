from sqlalchemy.orm import Session

from services.skill_service import (
    SkillService
)

from services.job_description_parser import (
    JobDescriptionParser
)

from services.ats_service import (
    ATSService
)


class ATSAnalysisService:

    @staticmethod
    def analyze_resume(
        db: Session,
        resume_id: int,
        job_description: str
    ):
        resume_skills = [
            skill.skill_name
            for skill in SkillService.get_resume_skills(
                db=db,
                resume_id=resume_id
            )
        ]

        required_skills = (
            JobDescriptionParser
            .extract_required_skills(
                job_description
            )
        )

        return ATSService.calculate_score(
            resume_skills,
            required_skills
        )
