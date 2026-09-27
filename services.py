from sqlalchemy import or_, select
from sqlalchemy.orm import Session

from .models import Student
from .vector_store import delete_student, upsert_student


def create_student(db: Session, data):
    student = Student(**data.model_dump())

    db.add(student)
    db.commit()
    db.refresh(student)

    upsert_student(student)

    return student


def list_students(
    db: Session,
    skip: int = 0,
    limit: int = 100
):
    return db.scalars(
        select(Student)
        .offset(skip)
        .limit(limit)
    ).all()


def get_student(
    db: Session,
    student_id: int
):
    return db.get(
        Student,
        student_id
    )


def search_students(
    db: Session,
    query: str
):
    pattern = f"%{query}%"

    return db.scalars(
        select(Student).where(
            or_(
                Student.name.ilike(pattern),
                Student.email.ilike(pattern),
                Student.course.ilike(pattern),
                Student.interests.ilike(pattern),
            )
        )
    ).all()


def update_student(
    db: Session,
    student_id: int,
    data
):
    student = get_student(
        db,
        student_id
    )

    if not student:
        return None

    updates = data.model_dump(
        exclude_unset=True
    )

    for key, value in updates.items():
        setattr(
            student,
            key,
            value
        )

    db.commit()
    db.refresh(student)

    upsert_student(student)

    return student


def delete_student_record(
    db: Session,
    student_id: int
):
    student = get_student(
        db,
        student_id
    )

    if not student:
        return False

    db.delete(student)
    db.commit()

    delete_student(student_id)

    return True