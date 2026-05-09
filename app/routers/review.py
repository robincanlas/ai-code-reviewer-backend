from fastapi import APIRouter
from app.models.review_models import ReviewRequest, ReviewResponse
from app.services.ai_service import review_code

router = APIRouter(prefix="/review", tags=["review"])

@router.post("", response_model=ReviewResponse)
def review(request: ReviewRequest):
    result = review_code(request.code, request.language)

    return ReviewResponse(review=result)