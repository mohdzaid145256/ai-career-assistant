from fastapi import (
    APIRouter,
    Depends
)

from database.dependencies import (
    get_current_user
)

from schemas.interview_answer import (
    InterviewAnswerRequest,
    InterviewAnswerResponse
)

from services.interview_answer_service import (
    InterviewAnswerService
)

router = APIRouter(
    prefix="/interview",
    tags=["Interview Answers"]
)


@router.post(
    "/answer",
    response_model=InterviewAnswerResponse
)
def get_answer(
    request: InterviewAnswerRequest,
    current_user=Depends(get_current_user)
):
    return {
        "answer":
        InterviewAnswerService.get_answer(
            request.question
        )
    }

