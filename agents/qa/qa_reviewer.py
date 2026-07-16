import json

from config import llm
from models import ReviewResult
from prompts.qa import reviewer_prompt


def qa_review(state):
    response = llm.invoke(reviewer_prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,code=state.code,test_cases=state.test_cases,) )

    if not response.content:
        raise ValueError("Failed to perform QA review.")

    review = ReviewResult.model_validate(
        json.loads(response.content)
    )

    state.qa_status = review.status.value
    state.code_feedback = review.feedback

    return state