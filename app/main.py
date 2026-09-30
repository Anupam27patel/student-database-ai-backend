from contextlib import asynccontextmanager

from fastapi import FastAPI

from .config import settings
from .database import Base, engine
from .routes_chatbot import router as chatbot_router
from .routes_students import router as student_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title=settings.app_name,
    version="1.0.0",
    description="Student CRUD backend with Gemini, LangGraph and ChromaDB.",
    lifespan=lifespan,
)


app.include_router(student_router)
app.include_router(chatbot_router)


@app.get(
    "/health",
    tags=["System"]
)
def health():
    return {
        "status": "ok",
        "service": settings.app_name,
    }
