from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from database.dependencies import (
    get_db,
    get_current_user
)

from schemas.resume_match import (
    ResumeMatchRequest,
    ResumeMatchResponse
)

from services.resume_match_service import (
    ResumeMatchService
)

router = APIRouter(
    prefix="/resume",
    tags=["Resume Match"]
)


@router.post(
    "/match",
    response_model=ResumeMatchResponse
)
def match_resume(
    request: ResumeMatchRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return {
        "analysis":
        ResumeMatchService.match_resume(
            db=db,
            resume_id=request.resume_id,
            job_description=request.job_description
        )
    }
