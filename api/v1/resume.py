import os
import shutil
from typing import List

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

from services.pdf_parser_service import (
    PDFParserService
)

from services.parsed_resume_service import (
    ParsedResumeService
)

from services.skill_extractor_service import (
    SkillExtractorService
)

from services.skill_service import (
    SkillService
)

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

    # Extract text from PDF
    raw_text = PDFParserService.extract_text(
        file_path
    )

    # Save parsed resume text
    ParsedResumeService.create_parsed_resume(
        db=db,
        resume_id=resume.id,
        raw_text=raw_text
    )

    # Extract skills
    skills = SkillExtractorService.extract_skills(
        raw_text
    )

    # Save skills
    for skill in skills:
        SkillService.create_skill(
            db=db,
            resume_id=resume.id,
            skill_name=skill
        )

    return resume


@router.get(
    "/list",
    response_model=List[ResumeResponse]
)
def list_resumes(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return ResumeService.get_user_resumes(
        db=db,
        user_id=current_user.id
    )


@router.get(
    "/{resume_id}",
    response_model=ResumeResponse
)
def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    resume = ResumeService.get_resume(
        db=db,
        resume_id=resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    if resume.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return resume


@router.delete("/{resume_id}")
def delete_resume(
    resume_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    resume = ResumeService.get_resume(
        db=db,
        resume_id=resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found"
        )

    if resume.user_id != current_user.id:
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    if os.path.exists(resume.file_path):
        os.remove(resume.file_path)

    ResumeService.delete_resume(
        db=db,
        resume=resume
    )

    return {
        "message": "Resume deleted successfully"
    }
