from pydantic import BaseModel
from typing import Optional

class InstructorCreate(BaseModel):
    name: str
    email: str
    bio: Optional[str] = None

class InstructorUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None

class Instructor(BaseModel):
    id: str
    name: str
    email: str
    bio: Optional[str] = None