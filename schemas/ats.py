from pydantic import BaseModel


class ATSRequest(BaseModel):
    resume_id: int
    job_description: str


class ATSResponse(BaseModel):
    score: float
    matched_skills: list[str]
    missing_skills: list[str]
