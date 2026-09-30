from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from .database import get_db
from .schemas import StudentCreate, StudentRead, StudentUpdate
from .services import (
    create_student,
    delete_student_record,
    get_student,
    list_students,
    search_students,
    update_student,
)


router = APIRouter(
    prefix="/students",
    tags=["Students"],
)


@router.post(
    "",
    response_model=StudentRead,
    status_code=201,
)
def create(
    data: StudentCreate,
    db: Session = Depends(get_db),
):
    return create_student(db, data)


@router.get(
    "",
    response_model=list[StudentRead],
)
def list_all(
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=100,
    ),
    q: str | None = None,
    db: Session = Depends(get_db),
):
    if q:
        return search_students(db, q)

    return list_students(
        db,
        skip,
        limit,
    )


@router.get(
    "/{student_id}",
    response_model=StudentRead,
)
def get_one(
    student_id: int,
    db: Session = Depends(get_db),
):
    student = get_student(
        db,
        student_id,
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student


@router.put(
    "/{student_id}",
    response_model=StudentRead,
)
def update(
    student_id: int,
    data: StudentUpdate,
    db: Session = Depends(get_db),
):
    student = update_student(
        db,
        student_id,
        data,
    )

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student


@router.delete(
    "/{student_id}",
)
def delete(
    student_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_student_record(
        db,
        student_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "message": "Student deleted",
        "id": student_id,
    }
