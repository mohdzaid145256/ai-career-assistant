from fastapi import (
    APIRouter,
    Depends
)
from sqlalchemy.orm import Session

from database.dependencies import (
    get_db,
    get_current_user
)

from schemas.ats import (
    ATSRequest,
    ATSResponse
)

from services.ats_analysis_service import (
    ATSAnalysisService
)

router = APIRouter(
    prefix="/ats",
    tags=["ATS"]
)


@router.post(
    "/analyze",
    response_model=ATSResponse
)
def analyze_resume(
    request: ATSRequest,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    result = ATSAnalysisService.analyze_resume(
        db=db,
        resume_id=request.resume_id,
        job_description=request.job_description
    )

    return result

