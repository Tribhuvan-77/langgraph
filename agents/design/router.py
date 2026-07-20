from state import State


def design_route(state: State):
    if state.design_count<=2:
      return state.design_status
    elif state.design_count>2:
       state.design_status="approved"
       return state.design_status