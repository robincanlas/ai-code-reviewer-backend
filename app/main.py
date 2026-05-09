from fastapi import FastAPI
from app.routers.review import router as review_router

app = FastAPI(
    title="AI Code Review Agent",
    version="1.0.0"
)

app.include_router(review_router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Code Review Backend Running"
    }