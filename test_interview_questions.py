from services.interview_question_service import (
    InterviewQuestionService
)

questions = (
    InterviewQuestionService
    .get_questions(
        "fastapi"
    )
)

print("=" * 50)
print("INTERVIEW QUESTIONS")
print("=" * 50)

for question in questions:
    print(question)
