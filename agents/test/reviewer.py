import json

from config import llm
from models import ReviewResult
from prompts.test import reviewer_prompt


def review_test(state):
    prompt=reviewer_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,code=state.code,test_cases=state.test_cases,))

    if not response.content:
        raise ValueError("Failed to review test cases.")

    review = ReviewResult.model_validate(
        json.loads(response.content)
    )

    state.test_status = review.status.value
    state.test_feedback = review.feedback

    return state