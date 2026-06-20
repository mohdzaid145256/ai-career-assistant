from pydantic import BaseModel


class InterviewAnswerRequest(BaseModel):
    question: str


class InterviewAnswerResponse(BaseModel):
    answer: str
