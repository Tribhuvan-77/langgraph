from langgraph.graph import StateGraph, START, END
from agents.user_story.generator import story
from agents.user_story.reviewer import review_story
from agents.user_story.reviser import revise_story
from agents.user_story.story_router import story_route
from agents.design.router import design_router
from agents.design.generator import design
from agents.design.reviewer import review_design
from agents.code.code_generator import code
from agents.code.code_reviewer import review_code
from agents.code.code_router import code_route
from agents.security.reviewer import review_security
from agents.security.security_route import security_route
from agents.test.generator import test
from agents.test.reviewer import review_test
from agents.test.test_router import test_route
from agents.qa.qa_reviewer import qa_review
from agents.qa.qa_router import qa_route
from state import State
from LongTermMem import add_memory
from checkpointer import checkpointers




graph = StateGraph(State)


graph.add_node("story",story)
graph.add_node("story_review",review_story)
graph.add_node("story_fix",revise_story)

graph.add_node("design",design)
graph.add_node("design_review",review_design)

graph.add_node("code",code)
graph.add_node("code_review",review_code)

graph.add_node("security_review",review_security)

graph.add_node("tests", test)
graph.add_node("test_review",review_test)


graph.add_node("qa",qa_review)


graph.add_node("deploy", lambda state: state)

graph.add_node("longterm_mem",add_memory)

graph.add_edge(START, "story")

graph.add_edge("story", "story_review")

graph.add_conditional_edges(
    "story_review",
    story_route,
    {
        "approved": "design",
        "feedback": "story_fix",
    },
)

graph.add_edge("story_review","longterm_mem")

graph.add_edge("story_fix", "story_review")

graph.add_edge("design", "design_review")

graph.add_edge("design_review","longterm_mem")

graph.add_conditional_edges(
    "design_review",
    design_router,
    {
        "approved": "code",
        "feedback": "design",
    },
)

graph.add_edge("code", "review_code")

graph.add_conditional_edges(
    "code_review",
    code_route,
    {
        "approved": "security_review",
        "feedback": "code",
    },
)


graph.add_conditional_edges(
    "security_review",
    security_route,
    {
        "approved": "tests",
        "feedback": "code",
    },
)


graph.add_edge("tests", "test_review")

graph.add_conditional_edges(
    "test_review",
    test_route,
    {
        "approved": "qa",
        "feedback": "tests",
    },
)


graph.add_conditional_edges(
    "qa",
    qa_route,
    {
        "approved": "deploy",
        "feedback": "code",
    },
)

graph.add_edge("deploy", END)


checkpointers.setup()

app = graph.compile(checkpointer=checkpointers)