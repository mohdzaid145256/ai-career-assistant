from sqlalchemy.orm import Session

from services.parsed_resume_service import (
    ParsedResumeService
)

from services.gemini_service import (
    GeminiService
)


class ResumeReviewService:

    @staticmethod
    def review_resume(
        db: Session,
        resume_id: int
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
You are a senior technical recruiter.

Review the following resume and provide:

1. Overall assessment
2. Strengths
3. Weaknesses
4. Improvements

Resume:

{parsed_resume.raw_text}
"""

        return GeminiService.generate_response(
            prompt
        )
