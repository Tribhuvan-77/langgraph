import json

from config import llm
from prompts.design import design_reviewer_prompt
from models import ReviewResult


def review_design(state):
    prompt=design_reviewer_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc))

    if not response.content:
        raise ValueError("Failed to review design document.")

    data = json.loads(response.content)

    review = ReviewResult.model_validate(data)

    state.design_status = review.status
    state.design_feedback = review.feedback

    return state