from fastapi import FastAPI

from api.v1.health import router as health_router

app = FastAPI(
    title="AI Career Assistant",
    version="1.0.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "AI Career Assistant API Running"
    }	
