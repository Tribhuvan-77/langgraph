from pydantic import BaseModel


class State(BaseModel):
    user_input: str = ""
    user_story: str = ""
    story_review: str = ""
    design_doc: str = ""
    design_review: str = ""
    code: str = ""
    code_review: str = ""
    security_review: str = ""
    test_cases: str = ""
    test_review: str = ""
    qa_result: str = ""
    deployment_status: bool=False