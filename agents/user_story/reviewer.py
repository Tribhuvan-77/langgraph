from config import llm
from prompts.user_story import reviewer_prompt
from models import Reviewresult
import json


def review_story(state):
    prompt=reviewer_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story))

    if not response.content:
        raise ValueError("Failed to review user stories.")

    result = response.content

    data=json.loads(result.content)
    review = Reviewresult.model_validate(data)

    if review.status=="approved":
        state.story_status = "approved"
        state.story_feedback = ""
    elif review.status=="feedback":
        state.story_status = "feedback"
        state.story_feedback =review.feedback

    return state