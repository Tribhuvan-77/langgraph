from config import llm
from prompts.user_story import generator_prompt


def story(state):
    prompt=generator_prompt
    try:
     response = llm.invoke(prompt.format(requirements=state.user_input))
    except Exception as e:
       print(e)
    if not response.content:
        raise ValueError("Failed to generate user stories.")

    state.user_story = response.content

    return state