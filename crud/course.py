from database import courses_collection
from bson import ObjectId

def course_helper(course) -> dict:
    return {
        "id": str(course["_id"]),
        "title": course["title"],
        "description": course.get("description", ""),
        "instructor_id": course["instructor_id"],
        "price": course["price"]
    }

def get_all_courses():
    courses = []
    for course in courses_collection.find():
        courses.append(course_helper(course))
    return courses

def create_course(course_data: dict):
    course = courses_collection.insert_one(course_data)
    new_course = courses_collection.find_one({"_id": course.inserted_id})
    return course_helper(new_course)

def get_course(course_id: str):
    course = courses_collection.find_one({"_id": ObjectId(course_id)})
    if course:
        return course_helper(course)
    return None

def update_course(course_id: str, course_data: dict):
    update_data = {k: v for k, v in course_data.items() if v is not None}
    
    if not update_data:
        return get_course(course_id)
    
    courses_collection.update_one(
        {"_id": ObjectId(course_id)},
        {"$set": update_data}
    )
    course = courses_collection.find_one({"_id": ObjectId(course_id)})
    if course:
        return course_helper(course)
    return None

def delete_course(course_id: str):
    result = courses_collection.delete_one({"_id": ObjectId(course_id)})
    return result.deleted_count > 0

def get_courses_by_instructor(instructor_id: str):
    courses = []
    for course in courses_collection.find({"instructor_id": instructor_id}):
        courses.append(course_helper(course))
    return courses
