from pydantic import BaseModel


class InterviewRequest(BaseModel):
    skill: str


class InterviewResponse(BaseModel):
    questions: list[str]
