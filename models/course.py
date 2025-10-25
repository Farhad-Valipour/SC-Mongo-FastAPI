from pydantic import BaseModel
from typing import Optional

class CourseCreate(BaseModel):
    title: str
    description: Optional[str] = None
    instructor_id: str  # ID مدرسی که دوره رو می‌سازه
    price: float

class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    instructor_id: Optional[str] = None
    price: Optional[float] = None

class Course(BaseModel):
    id: str
    title: str
    description: Optional[str] = None
    instructor_id: str
    price: float