from fastapi import FastAPI

from api.v1.auth import router as auth_router
from api.v1.resume import router as resume_router
from api.v1.ats import router as ats_router
from api.v1.interview import router as interview_router
from api.v1.interview_answer import (
    router as interview_answer_router
)

app = FastAPI(
    title="AI Career Assistant",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(interview_router)
app.include_router(interview_answer_router)


@app.get("/")
def root():
    return {
        "message": "AI Career Assistant API Running"
    }
