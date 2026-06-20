from fastapi import FastAPI

from api.v1.health import router as health_router
from api.v1.auth import router as auth_router

app = FastAPI(
    title="AI Career Assistant",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "AI Career Assistant API Running"
    }
