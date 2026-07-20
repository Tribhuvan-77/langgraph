import json

from config import llm
from models import CodeReviewResult
from prompts.code import code_reviewer_prompt


def review_code(state):
    prompt=code_reviewer_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,code=state.code))

    if not response.content:
        raise ValueError("Failed to review generated code.")
    
    print(repr(response.content))
    
    data=json.loads(response.content)

    review = CodeReviewResult.model_validate(data)

    state.code_status = review.status.value
    state.code_feedback = review.feedback
    state.code_count+=1

    return state