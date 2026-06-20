from services.gemini_service import (
    GeminiService
)


class InterviewAnswerService:

    @staticmethod
    def get_answer(
        question: str
    ):
        prompt = f"""
You are a senior software engineer.

Provide a professional interview answer
for the following question.

Question:
{question}

Keep the answer concise and suitable
for a job interview.
"""

        return GeminiService.generate_response(
            prompt
        )
