from fastapi import APIRouter, HTTPException
from models.enrollment import Enrollment, EnrollmentCreate
from models.course import Course
from models.student import Student
from crud.enrollment import (
    get_all_enrollments,
    create_enrollment as crud_create_enrollment,
    delete_enrollment as crud_delete_enrollment,
    get_student_courses,
    get_course_students
)
from crud.course import get_course
from crud.student import get_student

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.get("/", response_model=list[Enrollment])
def list_enrollments():
    return get_all_enrollments()

@router.post("/", response_model=Enrollment)
def create_enrollment(enrollment: EnrollmentCreate):
    result = crud_create_enrollment(enrollment.dict())
    if not result:
        raise HTTPException(status_code=400, detail="Student already enrolled in this course")
    return result

@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: str):
    deleted = crud_delete_enrollment(enrollment_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return {"message": "Enrollment deleted successfully"}

@router.get("/students/{student_id}/courses/", response_model=list[Course])
def get_student_enrolled_courses(student_id: str):
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    enrollments = get_student_courses(student_id)
    
    courses = []
    for enrollment in enrollments:
        course = get_course(enrollment["course_id"])
        if course:
            courses.append(course)
    
    return courses

@router.get("/courses/{course_id}/students/", response_model=list[Student])
def get_course_enrolled_students(course_id: str):
    course = get_course(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    enrollments = get_course_students(course_id)
    
    students = []
    for enrollment in enrollments:
        student = get_student(enrollment["student_id"])
        if student:
            students.append(student)
    
    return students