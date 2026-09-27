from fastapi import APIRouter, HTTPException

from .config import settings
from .graph import graph
from .schemas import ChatRequest, ChatResponse


router = APIRouter(
    prefix="/chat",
    tags=["AI Chatbot"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):

    if not settings.gemini_api_key:
        raise HTTPException(
            status_code=500,
            detail="GEMINI_API_KEY is not configured.",
        )

    result = graph.invoke({
        "messages": [
            {
                "role": "user",
                "content": request.message,
            }
        ]
    })

    final_message = result["messages"][-1]

    content = final_message.content

    if isinstance(content, list):
        content = " ".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict)
        )

    return ChatResponse(
        answer=str(content)
    )