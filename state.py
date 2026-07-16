from pydantic import BaseModel


class State(BaseModel):
    user_input: str = ""
    user_id:str=""
    user_story: str = ""

    story_status:str= ""
    story_feedback: str = ""

    design_doc: str = ""
    design_status: str = ""
    design_feedback:str= ""

    code: str = ""
    code_status: str = ""
    code_feedback:str= ""

    security_status: str = ""
    security_feedback:str = ""

    test_cases: str = ""
    test_status: str = ""
    test_feedback:str=""

    qa_status: str = ""
    qa_feedback:str=""
    
    deployment_status: bool=False