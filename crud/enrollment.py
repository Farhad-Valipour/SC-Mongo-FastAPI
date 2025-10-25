from database import enrollments_collection
from bson import ObjectId
from datetime import datetime

def enrollment_helper(enrollment) -> dict:
    return {
        "id": str(enrollment["_id"]),
        "student_id": enrollment["student_id"],
        "course_id": enrollment["course_id"],
        "enrolled_at": enrollment["enrolled_at"]
    }

def get_all_enrollments():
    enrollments = []
    for enrollment in enrollments_collection.find():
        enrollments.append(enrollment_helper(enrollment))
    return enrollments

def create_enrollment(enrollment_data: dict):
    existing = enrollments_collection.find_one({
        "student_id": enrollment_data["student_id"],
        "course_id": enrollment_data["course_id"]
    })
    
    if existing:
        return None
    
    enrollment_data["enrolled_at"] = datetime.now().isoformat()
    
    enrollment = enrollments_collection.insert_one(enrollment_data)
    new_enrollment = enrollments_collection.find_one({"_id": enrollment.inserted_id})
    return enrollment_helper(new_enrollment)

def delete_enrollment(enrollment_id: str):
    result = enrollments_collection.delete_one({"_id": ObjectId(enrollment_id)})
    return result.deleted_count > 0

def get_student_courses(student_id: str):
    enrollments = []
    for enrollment in enrollments_collection.find({"student_id": student_id}):
        enrollments.append(enrollment_helper(enrollment))
    return enrollments

def get_course_students(course_id: str):
    enrollments = []
    for enrollment in enrollments_collection.find({"course_id": course_id}):
        enrollments.append(enrollment_helper(enrollment))
    return enrollments
