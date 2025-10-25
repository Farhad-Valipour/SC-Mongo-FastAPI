from fastapi import FastAPI
from routers import instructor, student, course, enrollment

app = FastAPI(title="Course Selling API")

app.include_router(instructor.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(enrollment.router)

@app.get("/")
def root():
    return {"message": "Welcome to Course Selling API"}