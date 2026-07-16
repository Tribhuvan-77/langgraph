from config import llm
from prompts.test import generator_prompt


def test(state):
    prompt=generator_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input,user_story=state.user_story,design=state.design_doc,code=state.code,))

    if not response.content:
        raise ValueError("Failed to generate test cases.")

    state.test_cases = response.content

    return state