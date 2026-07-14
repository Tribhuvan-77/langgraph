from config import llm
from prompts.user_story import generator_prompt


def story(state):
    prompt=generator_prompt
    response = llm.invoke(prompt.format(requirements=state.user_input))

    if not response.content:
        raise ValueError("Failed to generate user stories.")

    state.user_story = response.content

    return state