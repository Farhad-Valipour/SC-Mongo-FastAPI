from database import instructors_collection
from bson import ObjectId

def instructor_helper(instructor) -> dict:
    return {
        "id": str(instructor["_id"]),
        "name": instructor["name"],
        "email": instructor["email"],
        "bio": instructor.get("bio", "")
    }

def get_all_instructors():
    instructors = []
    for instructor in instructors_collection.find():
        instructors.append(instructor_helper(instructor))
    return instructors

def create_instructor(instructor_data: dict):
    instructor = instructors_collection.insert_one(instructor_data)
    new_instructor = instructors_collection.find_one({"_id": instructor.inserted_id})
    return instructor_helper(new_instructor)

def get_instructor(instructor_id: str):
    instructor = instructors_collection.find_one({"_id": ObjectId(instructor_id)})
    if instructor:
        return instructor_helper(instructor)
    return None

def update_instructor(instructor_id: str, instructor_data: dict):
    # فقط فیلدهایی که مقدار دارن رو آپدیت کن
    # فیلدهای None رو حذف می‌کنیم
    update_data = {k: v for k, v in instructor_data.items() if v is not None}
    
    # اگه هیچ چیزی برای آپدیت نیست، همون قبلی رو برگردون
    if not update_data:
        return get_instructor(instructor_id)
    
    instructors_collection.update_one(
        {"_id": ObjectId(instructor_id)},
        {"$set": update_data}
    )
    instructor = instructors_collection.find_one({"_id": ObjectId(instructor_id)})
    if instructor:
        return instructor_helper(instructor)
    return None

def delete_instructor(instructor_id: str):
    result = instructors_collection.delete_one({"_id": ObjectId(instructor_id)})
    return result.deleted_count > 0