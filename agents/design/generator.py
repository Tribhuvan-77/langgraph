from config import llm
from prompts.design import design_generator_prompt


def design(state):
    prompt=design_generator_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,feedback=state.design_feedback))
    
    if not response.content:
        raise ValueError("Failed to generate design document.")

    state.design_doc = response.content

    return state