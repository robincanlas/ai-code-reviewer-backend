from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.review_models import ReviewRequest, ReviewResponse
from app.services.ai_service import review_code, stream_review_code

router = APIRouter(prefix="/review", tags=["review"])

@router.post("", response_model=ReviewResponse)
def review(request: ReviewRequest):
    result = review_code(request.code, request.language)

    return ReviewResponse(review=result)

@router.post("/stream")
def review_stream(request: ReviewRequest):
    generator = stream_review_code(
        request.code,
        request.language,
    )

    return StreamingResponse(
        generator,
        media_type="text/plain",
    )