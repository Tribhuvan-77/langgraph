from pydantic import BaseModel,Field


class State(BaseModel):
    user_input: str = ""
    user_id:str=""
    user_story: str = ""

    story_status:str= ""
    story_feedback: str = ""
    story_count:int=0

    design_doc: str = ""
    design_status: str = ""
    design_feedback:list[str]=Field(default_factory=list)
    design_count:int=0

    code: str = ""
    code_status: str = ""
    code_feedback:list[str]=Field(default_factory=list)
    code_count:int=0


    security_status: str = ""
    security_feedback:str = ""
    security_count:int=0

    test_cases: str = ""
    test_status: str = ""
    test_feedback:str=""
    test_count:int=0

    qa_status: str = ""
    qa_feedback:str=""
    qa_count:int=0

    deployment_status: bool=False