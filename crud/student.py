from database import students_collection
from bson import ObjectId

def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "email": student["email"],
        "phone": student.get("phone", "")
    }

def get_all_students():
    students = []
    for student in students_collection.find():
        students.append(student_helper(student))
    return students

def create_student(student_data: dict):
    student = students_collection.insert_one(student_data)
    new_student = students_collection.find_one({"_id": student.inserted_id})
    return student_helper(new_student)

def get_student(student_id: str):
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)
    return None

def update_student(student_id: str, student_data: dict):
    update_data = {k: v for k, v in student_data.items() if v is not None}
    
    if not update_data:
        return get_student(student_id)
    
    students_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": update_data}
    )
    student = students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)
    return None

def delete_student(student_id: str):
    result = students_collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0