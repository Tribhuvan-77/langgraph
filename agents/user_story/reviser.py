from config import llm
from prompts.user_story import revisor_prompt


def revise_story(state):
    prompt=revisor_prompt
    try:
     response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,feedback=state.story_feedback))
    except Exception as e:
       print(e)
    if not response.content:
        raise ValueError("Failed to revise user stories.")

    state.user_story = response.content

    return state
