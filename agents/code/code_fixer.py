from config import llm
from prompts.code import code_fixer_prompt


def fix_code(state):
    prompt=code_fixer_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,code=state.code,feedback=state.code_feedback,))

    if not response.content:
        raise ValueError("Failed to improve code.")

    state.code = response.content

    return state