from sqlalchemy.orm import Session

from services.parsed_resume_service import (
    ParsedResumeService
)

from services.gemini_service import (
    GeminiService
)


class ResumeMatchService:

    @staticmethod
    def match_resume(
        db: Session,
        resume_id: int,
        job_description: str
    ):
        parsed_resume = (
            ParsedResumeService
            .get_by_resume_id(
                db=db,
                resume_id=resume_id
            )
        )

        if not parsed_resume:
            return "Resume not found."

        prompt = f"""
You are an expert technical recruiter.

Compare the resume with the job description.

Provide:

1. Match Score (0-100)
2. Strengths
3. Missing Skills
4. Recommended Improvements

Resume:
{parsed_resume.raw_text}

Job Description:
{job_description}
"""

        return GeminiService.generate_response(
            prompt
        )
