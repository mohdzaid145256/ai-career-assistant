import os
import shutil

from fastapi import (
    APIRouter,
    Depends,
    File,
    HTTPException,
    UploadFile
)
from sqlalchemy.orm import Session

from database.dependencies import (
    get_db,
    get_current_user
)

from schemas.resume import ResumeResponse
from services.resume_service import ResumeService

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.post(
    "/upload",
    response_model=ResumeResponse
)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    os.makedirs(
        "uploads/resumes",
        exist_ok=True
    )

    file_path = (
        f"uploads/resumes/"
        f"{current_user.id}_{file.filename}"
    )

    with open(
        file_path,
        "wb"
    ) as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    file_size = os.path.getsize(
        file_path
    )

    resume = ResumeService.create_resume(
        db=db,
        user_id=current_user.id,
        file_name=file.filename,
        file_path=file_path,
        file_size=file_size
    )

    return resume
