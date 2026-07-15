from langgraph.graph import StateGraph, START, END
from agents.user_story.generator import story
from agents.user_story.reviewer import review_story
from agents.user_story.reviser import revise_story
from agents.user_story.story_router import story_route
from agents.design.router import design_router
from agents.design.generator import design
from agents.design.reviewer import review_design
from state import State
from checkpointer import checkpointers




graph = StateGraph(State)


graph.add_node("story",story)
graph.add_node("story_review",review_story)
graph.add_node("story_fix",revise_story)

graph.add_node("design",design)
graph.add_node("design_review",review_design)

graph.add_node("code", lambda state: state)
graph.add_node("code_review", lambda state: state)
graph.add_node("code_fix", lambda state: state)

graph.add_node("security", lambda state: state)
graph.add_node("security_fix", lambda state: state)

graph.add_node("tests", lambda state: state)
graph.add_node("test_review", lambda state: state)
graph.add_node("test_fix", lambda state: state)

graph.add_node("qa", lambda state: state)
graph.add_node("qa_fix", lambda state: state)

graph.add_node("deploy", lambda state: state)


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

graph.add_edge("story_fix", "story")

graph.add_edge("design", "design_review")

graph.add_conditional_edges(
    "design_review",
    design_router,
    {
        "approved": "code",
        "feedback": "design",
    },
)

graph.add_edge("code", "code_review")

graph.add_conditional_edges(
    "code_review",
    code_route,
    {
        "next": "security",
        "fix": "code_fix",
    },
)

graph.add_edge("code_fix", "code")

graph.add_conditional_edges(
    "security",
    security_route,
    {
        "next": "tests",
        "fix": "security_fix",
    },
)

graph.add_edge("security_fix", "code")

graph.add_edge("tests", "test_review")

graph.add_conditional_edges(
    "test_review",
    test_route,
    {
        "next": "qa",
        "fix": "test_fix",
    },
)

graph.add_edge("test_fix", "tests")

graph.add_conditional_edges(
    "qa",
    qa_route,
    {
        "next": "deploy",
        "fix": "qa_fix",
    },
)

graph.add_edge("qa_fix", "code")

graph.add_edge("deploy", END)


checkpointers.setup()

app = graph.compile(checkpointer=checkpointers)