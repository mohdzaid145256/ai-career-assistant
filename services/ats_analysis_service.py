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

from services.recommendation_service import (
    RecommendationService
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

        result = ATSService.calculate_score(
            resume_skills,
            required_skills
        )

        result["recommendations"] = (
            RecommendationService
            .generate_recommendations(
                result["missing_skills"]
            )
        )

        return result
