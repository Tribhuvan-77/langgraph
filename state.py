from pydantic import BaseModel


class State(BaseModel):
    user_input: str = ""
    user_story: str = ""

    story_status:str= ""
    story_feedback: str = ""

    design_doc: str = ""
    design_status: str = ""
    design_feedback:str= ""

    code: str = ""
    code_review: str = ""
    code_feedback:str= ""

    security_review: str = ""
    security_feedback:str = ""

    test_cases: str = ""
    test_review: str = ""
    test_feedback:str=""

    qa_result: str = ""
    qa_feedback:str=""
    
    deployment_status: bool=False