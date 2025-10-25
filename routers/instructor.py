from fastapi import APIRouter, HTTPException
from models.instructor import Instructor, InstructorCreate, InstructorUpdate
from models.course import Course
from crud.instructor import (
    get_all_instructors,
    create_instructor as crud_create_instructor,
    get_instructor as crud_get_instructor,
    update_instructor as crud_update_instructor,
    delete_instructor as crud_delete_instructor
)
from crud.course import get_courses_by_instructor

router = APIRouter(prefix="/instructors", tags=["Instructors"])

@router.get("/", response_model=list[Instructor])
def list_instructors():
    return get_all_instructors()

@router.post("/", response_model=Instructor)
def create_instructor(instructor: InstructorCreate):
    return crud_create_instructor(instructor.dict())

@router.get("/{instructor_id}", response_model=Instructor)
def get_instructor(instructor_id: str):
    instructor = crud_get_instructor(instructor_id)
    if not instructor:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return instructor

@router.put("/{instructor_id}", response_model=Instructor)
def update_instructor(instructor_id: str, instructor: InstructorUpdate):
    updated = crud_update_instructor(instructor_id, instructor.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return updated

@router.delete("/{instructor_id}")
def delete_instructor(instructor_id: str):
    deleted = crud_delete_instructor(instructor_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Instructor not found")
    return {"message": "Instructor deleted successfully"}

@router.get("/{instructor_id}/courses/", response_model=list[Course])
def get_instructor_courses(instructor_id: str):
    return get_courses_by_instructor(instructor_id)