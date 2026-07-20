import json

from config import llm
from prompts.design import design_reviewer_prompt
from models import DocReviewResult


def review_design(state):
    prompt=design_reviewer_prompt
    try:
     response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc))
    except Exception as e:
       print(e)
    if not response.content:
        raise ValueError("Failed to review design document.")
    
    print(response.content)

    data = json.loads(response.content)

    review = DocReviewResult.model_validate(data)

    state.design_status = review.status
    state.design_feedback = review.feedback
    state.design_count+=1

    return state
