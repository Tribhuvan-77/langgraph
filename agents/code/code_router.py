from state import State

def code_route(state: State):
    if state.code_count<2:
      return state.code_status
    elif state.code_count>2:
       state.code_status="approved"
       return state.code_status