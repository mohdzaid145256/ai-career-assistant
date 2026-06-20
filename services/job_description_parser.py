from services.skill_extractor_service import (
    SkillExtractorService
)


class JobDescriptionParser:

    @staticmethod
    def extract_required_skills(
        job_description: str
    ):
        return SkillExtractorService.extract_skills(
            job_description
        )
