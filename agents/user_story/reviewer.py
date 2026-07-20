from config import llm
from prompts.user_story import reviewer_prompt
from models import ReviewResult
import json


def review_story(state):
    prompt=reviewer_prompt
    try:
     response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story))
     if not response.content:
           raise ValueError("Failed to review user stories.")
    except Exception as e :
       print(e)

    result=response.content
    print(result)


    data=json.loads(result)
    review = ReviewResult.model_validate(data)

    if review.status=="approved":
        state.story_status = "approved"
        state.story_feedback = ""
    elif review.status=="feedback":
        state.story_status = "feedback"
        state.story_feedback =review.feedback
        state.story_count+=1

    return state