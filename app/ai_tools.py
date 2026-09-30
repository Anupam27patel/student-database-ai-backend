from langchain_core.tools import tool
from sqlalchemy import or_, select

from .database import SessionLocal
from .models import Student
from .vector_store import semantic_search


def _student_dict(student: Student) -> dict:
    return {
        "id": student.id,
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "course": student.course,
        "year": student.year,
        "marks": student.marks,
        "interests": student.interests,
    }


@tool
def search_student_database(query: str) -> str:
    """Search structured student records by name, email, course, or interest."""
    with SessionLocal() as db:
        pattern = f"%{query}%"

        rows = db.scalars(
            select(Student).where(
                or_(
                    Student.name.ilike(pattern),
                    Student.email.ilike(pattern),
                    Student.course.ilike(pattern),
                    Student.interests.ilike(pattern),
                )
            )
        ).all()

    if not rows:
        return "No structured student record matched the query."

    return str([
        _student_dict(row)
        for row in rows[:20]
    ])


@tool
def semantic_student_search(query: str) -> str:
    """Find students using semantic/vector similarity search."""
    docs = semantic_search(
        query,
        n_results=5
    )

    if not docs:
        return "No vector-search results are available."

    return "\n".join(docs)


@tool
def get_student_by_id(student_id: int) -> str:
    """Get one student record by numeric student ID."""
    with SessionLocal() as db:
        student = db.get(
            Student,
            student_id
        )

    if not student:
        return "Student not found."

    return str(
        _student_dict(student)
    )
