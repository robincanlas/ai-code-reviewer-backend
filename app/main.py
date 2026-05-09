from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.review import router as review_router

app = FastAPI(
    title="AI Code Review Agent",
    version="1.0.0"
)

# ✅ Allowed frontend origins
origins = [
    "http://localhost:5173",
]

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],
)

app.include_router(review_router)

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Code Review Backend Running"
    }