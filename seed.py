from app.database import Base, SessionLocal, engine
from app.models import Student
from app.vector_store import upsert_student


Base.metadata.create_all(bind=engine)


students = [
    Student(
        name="Rahul Kumar",
        email="rahul@example.com",
        course="BTech CSE",
        year=2,
        marks=82,
        interests="machine learning, web development",
    ),
    Student(
        name="Priya Singh",
        email="priya@example.com",
        course="BTech ECE",
        year=3,
        marks=88,
        interests="embedded systems, robotics",
    ),
    Student(
        name="Aman Verma",
        email="aman@example.com",
        course="BTech CSE",
        year=2,
        marks=76,
        interests="cybersecurity, Python",
    ),
]


with SessionLocal() as db:
    for student in students:

        existing = db.query(Student).filter(
            Student.email == student.email
        ).first()

        if existing:
            continue

        db.add(student)
        db.commit()
        db.refresh(student)

        upsert_student(student)


print("Seed complete.")