from enum import Enum
from pydantic import BaseModel



class ReviewStatus(str, Enum):
    approved = "approved"
    feedback = "feedback"


class ReviewResult(BaseModel):
    status: ReviewStatus
    feedback: str

class DocReviewResult(BaseModel):
    status: ReviewStatus
    feedback: list[str]

class CodeReviewResult(BaseModel):
    status: ReviewStatus
    feedback: list[str]