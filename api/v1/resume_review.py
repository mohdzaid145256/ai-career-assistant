from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import (
    get_db,
    get_current_user
)

from schemas.resume_review import (
    ResumeReviewRequest,
    ResumeReviewResponse
)

from services.resume_review_service import (
    ResumeReviewService
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Review"]
)


@router.post(
    "/review",
    response_model=ResumeReviewResponse
)
def review_resume(
    request: ResumeReviewRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return {
        "review":
        ResumeReviewService.review_resume(
            db=db,
            resume_id=request.resume_id
        )
    }
