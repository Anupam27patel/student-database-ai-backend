import chromadb

from .config import settings


client = chromadb.PersistentClient(
    path=settings.chroma_path
)

collection = client.get_or_create_collection(
    name=settings.chroma_collection
)


def student_to_document(student) -> str:
    return (
        f"Student ID: {student.id}. "
        f"Name: {student.name}. "
        f"Email: {student.email}. "
        f"Course: {student.course}. "
        f"Year: {student.year}. "
        f"Marks: {student.marks}. "
        f"Interests: {student.interests or 'not specified'}."
    )


def upsert_student(student) -> None:
    collection.upsert(
        ids=[str(student.id)],
        documents=[student_to_document(student)],
        metadatas=[{
            "student_id": student.id,
            "name": student.name,
            "course": student.course,
            "year": student.year,
        }],
    )


def delete_student(student_id: int) -> None:
    collection.delete(
        ids=[str(student_id)]
    )


def semantic_search(
    query: str,
    n_results: int = 5
) -> list[str]:
    if collection.count() == 0:
        return []

    results = collection.query(
        query_texts=[query],
        n_results=min(
            n_results,
            collection.count()
        ),
    )

    return results.get(
        "documents",
        [[]]
    )[0]
