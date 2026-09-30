from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import END, MessagesState, START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from .ai_tools import (
    get_student_by_id,
    search_student_database,
    semantic_student_search,
)
from .config import settings


tools = [
    search_student_database,
    semantic_student_search,
    get_student_by_id,
]


llm = ChatGoogleGenerativeAI(
    model=settings.gemini_model,
    google_api_key=settings.gemini_api_key,
    temperature=0,
)


llm_with_tools = llm.bind_tools(tools)


SYSTEM_PROMPT = """
You are the Student Database AI Assistant.

You can answer general questions, but when the user asks about student
records, use the provided database tools instead of inventing data.

Use:
- search_student_database for exact/structured student searches.
- semantic_student_search for meaning-based or interest-based searches.
- get_student_by_id when a numeric student ID is provided.

Never invent a student record.
Do not expose API keys or internal secrets.

For destructive database operations, this demo provides no delete tool;
deletion must be performed through the protected REST API.
"""


def call_model(state: MessagesState):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT)
    ] + state["messages"]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }


workflow = StateGraph(MessagesState)

workflow.add_node(
    "assistant",
    call_model
)

workflow.add_node(
    "tools",
    ToolNode(tools)
)

workflow.add_edge(
    START,
    "assistant"
)

workflow.add_conditional_edges(
    "assistant",
    tools_condition,
    {
        "tools": "tools",
        END: END,
    },
)

workflow.add_edge(
    "tools",
    "assistant"
)


graph = workflow.compile()
