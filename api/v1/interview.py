from fastapi import (
    APIRouter,
    Depends
)

from database.dependencies import (
    get_current_user
)

from schemas.interview import (
    InterviewRequest,
    InterviewResponse
)

from services.interview_question_service import (
    InterviewQuestionService
)

router = APIRouter(
    prefix="/interview",
    tags=["Interview"]
)


@router.post(
    "/questions",
    response_model=InterviewResponse
)
def get_questions(
    request: InterviewRequest,
    current_user=Depends(get_current_user)
):
    return {
        "questions":
        InterviewQuestionService.get_questions(
            request.skill
        )
    }
