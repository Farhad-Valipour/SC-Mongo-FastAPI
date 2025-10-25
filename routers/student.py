from fastapi import APIRouter, HTTPException
from models.student import Student, StudentCreate, StudentUpdate
from models.course import Course
from crud.student import (
    get_all_students,
    create_student as crud_create_student,
    get_student as crud_get_student,
    update_student as crud_update_student,
    delete_student as crud_delete_student
)
from crud.enrollment import get_student_courses
from crud.course import get_course

router = APIRouter(prefix="/students", tags=["Students"])

@router.get("/", response_model=list[Student])
def list_students():
    return get_all_students()

@router.post("/", response_model=Student)
def create_student(student: StudentCreate):
    return crud_create_student(student.dict())

@router.get("/{student_id}", response_model=Student)
def get_student(student_id: str):
    student = crud_get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=Student)
def update_student(student_id: str, student: StudentUpdate):
    updated = crud_update_student(student_id, student.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated

@router.delete("/{student_id}")
def delete_student(student_id: str):
    deleted = crud_delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

@router.get("/{student_id}/courses/", response_model=list[Course])
def get_student_enrolled_courses(student_id: str):
    enrollments = get_student_courses(student_id)
    courses = []
    for enrollment in enrollments:
        course = get_course(enrollment["course_id"])
        if course:
            courses.append(course)
    return courses