from pydantic import BaseModel


class ResumeReviewRequest(BaseModel):
    resume_id: int


class ResumeReviewResponse(BaseModel):
    review: str
