from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class StudentBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )

    email: str = Field(
        min_length=3,
        max_length=150,
    )

    phone: str | None = None

    course: str = Field(
        min_length=2,
        max_length=100,
    )

    year: int = Field(
        ge=1,
        le=8,
    )

    marks: int = Field(
        default=0,
        ge=0,
        le=100,
    )

    interests: str | None = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    email: str | None = Field(
        default=None,
        min_length=3,
        max_length=150,
    )

    phone: str | None = None

    course: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    year: int | None = Field(
        default=None,
        ge=1,
        le=8,
    )

    marks: int | None = Field(
        default=None,
        ge=0,
        le=100,
    )

    interests: str | None = None


class StudentRead(StudentBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=2000,
    )


class ChatResponse(BaseModel):
    answer: str
