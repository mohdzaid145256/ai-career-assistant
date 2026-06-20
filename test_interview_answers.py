from services.interview_answer_service import (
    InterviewAnswerService
)

answer = (
    InterviewAnswerService
    .get_answer(
        "What is FastAPI?"
    )
)

print("=" * 50)
print("ANSWER")
print("=" * 50)
print(answer)
