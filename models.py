from datetime import datetime

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        index=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    course: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    year: Mapped[int] = mapped_column(
        Integer,
        index=True,
    )

    marks: Mapped[int] = mapped_column(
        Integer,
        default=0,
    )

    interests: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )