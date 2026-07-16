import json

from config import llm
from models import ReviewResult
from prompts.security import security_reviewer_prompt


def review_security(state):
    prompt=security_reviewer_prompt
    response = llm.invoke(
        prompt.format(
            requirements=state.user_input,
            user_story=state.user_story,
            design=state.design_doc,
            code=state.code,
        )
    )

    if not response.content:
        raise ValueError("Failed to review code security.")

    review = ReviewResult.model_validate(
        json.loads(response.content)
    )

    state.security_status = review.status.value
    state.security_feedback = review.feedback

    return state