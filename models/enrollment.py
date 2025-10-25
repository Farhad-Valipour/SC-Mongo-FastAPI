from pydantic import BaseModel
from datetime import datetime

class EnrollmentCreate(BaseModel):
    student_id: str
    course_id: str

class Enrollment(BaseModel):
    id: str
    student_id: str
    course_id: str
    enrolled_at: str  # تاریخ ثبت‌نام