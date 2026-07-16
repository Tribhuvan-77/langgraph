from enum import Enum
from pydantic import BaseModel


class Reviewresult(str, Enum):
    approved = "approved"
    feedback = "feedback"


class StoryReview(BaseModel):
    status: Reviewresult
    feedback: str



class ReviewStatus(str, Enum):
    approved = "approved"
    feedback = "feedback"


class ReviewResult(BaseModel):
    status: ReviewStatus
    feedback: str

