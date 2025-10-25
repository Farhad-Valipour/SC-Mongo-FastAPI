from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["course_db"]

instructors_collection = db["instructors"]
students_collection = db["students"]
courses_collection = db["courses"]
enrollments_collection = db["enrollments"]