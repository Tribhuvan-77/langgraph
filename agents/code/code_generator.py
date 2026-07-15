from config import llm
from prompts.code import code_generator_prompt


def code(state):
    prompt=code_generator_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,))
    if not response.content:
        raise ValueError("Failed to generate code.")

    state.code = response.content

    return state