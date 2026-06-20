from pydantic import BaseModel


class ResumeMatchRequest(BaseModel):
    resume_id: int
    job_description: str


class ResumeMatchResponse(BaseModel):
    analysis: str
