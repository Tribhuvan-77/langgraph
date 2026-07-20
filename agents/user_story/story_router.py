from state import State
from langgraph.types import interrupt

def story_route(state: State):
    if state.story_count<=2:
      return state.story_status
    elif state.story_count>2:
       state.story_status="approved"
       return state.story_status
    # #    human_response=interrupt({"story":state.user_story})
    #    if human_response.lower()=="no":
    #       raise RuntimeError("Max tried completed --> restart")
    #    elif human_response.lower()=="yes":
    #       state.story_status="approved"
          