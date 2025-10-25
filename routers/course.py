from fastapi import APIRouter, HTTPException
from models.course import Course, CourseCreate, CourseUpdate
from models.student import Student
from crud.course import (
    get_all_courses,
    create_course as crud_create_course,
    get_course as crud_get_course,
    update_course as crud_update_course,
    delete_course as crud_delete_course,
    get_courses_by_instructor
)
from crud.enrollment import get_course_students
from crud.student import get_student

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=list[Course])
def list_courses():
    return get_all_courses()

@router.post("/", response_model=Course)
def create_course(course: CourseCreate):
    return crud_create_course(course.dict())

@router.get("/{course_id}", response_model=Course)
def get_course(course_id: str):
    course = crud_get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=Course)
def update_course(course_id: str, course: CourseUpdate):
    updated = crud_update_course(course_id, course.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated

@router.delete("/{course_id}")
def delete_course(course_id: str):
    deleted = crud_delete_course(course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}

@router.get("/{course_id}/students/", response_model=list[Student])
def get_course_enrolled_students(course_id: str):
    enrollments = get_course_students(course_id)
    students = []
    for enrollment in enrollments:
        student = get_student(enrollment["student_id"])
        if student:
            students.append(student)
    return students