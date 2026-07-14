from enum import Enum
from pydantic import BaseModel


class Reviewresult(str, Enum):
    approved = "approved"
    feedback = "feedback"


class StoryReview(BaseModel):
    status: Reviewresult
    feedback: str
