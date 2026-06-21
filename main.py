from fastapi import FastAPI

from database.base import Base
from database.session import engine
import models

from api.v1.auth import router as auth_router
from api.v1.resume import router as resume_router
from api.v1.ats import router as ats_router
from api.v1.interview import router as interview_router
from api.v1.interview_answer import (
router as interview_answer_router
)
from api.v1.resume_review import (
router as resume_review_router
)
from api.v1.resume_match import (
router as resume_match_router
)

# Create tables automatically

Base.metadata.create_all(bind=engine)

app = FastAPI(
title="AI Career Assistant",
version="1.0.0"
)

app.include_router(auth_router)
app.include_router(resume_router)
app.include_router(ats_router)
app.include_router(interview_router)
app.include_router(interview_answer_router)
app.include_router(resume_review_router)
app.include_router(resume_match_router)

@app.get("/")
def root():
return {
"message": "AI Career Assistant API Running"
}

