from pymongo import MongoClient
from datetime import datetime

# اتصال به MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["course_db"]

# پاک کردن دیتاهای قبلی (اختیاری)
"""print("🗑️  پاک کردن دیتاهای قبلی...")
db["instructors"].delete_many({})
db["students"].delete_many({})
db["courses"].delete_many({})
db["enrollments"].delete_many({})"""

# ========================================
# 📘 مدرس‌ها (5 نفر)
# ========================================
print("👨‍🏫 اضافه کردن مدرس‌ها...")

instructors = [
    {
        "name": "دکتر علی احمدی",
        "email": "ali.ahmadi@example.com",
        "bio": "استاد برنامه‌نویسی با 10 سال سابقه تدریس"
    },
    {
        "name": "دکتر سارا محمدی",
        "email": "sara.mohammadi@example.com",
        "bio": "متخصص هوش مصنوعی و یادگیری ماشین"
    },
    {
        "name": "مهندس رضا کریمی",
        "email": "reza.karimi@example.com",
        "bio": "توسعه‌دهنده وب با تجربه در React و Node.js"
    },
    {
        "name": "دکتر مریم حسینی",
        "email": "maryam.hosseini@example.com",
        "bio": "استاد علوم داده و تحلیل آماری"
    },
    {
        "name": "مهندس حسین رضایی",
        "email": "hosein.rezaei@example.com",
        "bio": "معماری نرم‌افزار و طراحی سیستم‌های توزیع‌شده"
    }
]

instructor_ids = []
for instructor in instructors:
    result = db["instructors"].insert_one(instructor)
    instructor_ids.append(str(result.inserted_id))
    print(f"   ✅ {instructor['name']} اضافه شد")

# ========================================
# 📗 دانشجوها (5 نفر)
# ========================================
print("\n👨‍🎓 اضافه کردن دانشجوها...")

students = [
    {
        "name": "محمد علیزاده",
        "email": "mohammad.alizadeh@student.com",
        "phone": "09121234567"
    },
    {
        "name": "فاطمه کاظمی",
        "email": "fatemeh.kazemi@student.com",
        "phone": "09129876543"
    },
    {
        "name": "امیر حسین پور",
        "email": "amir.hoseinpour@student.com",
        "phone": "09131112222"
    },
    {
        "name": "زهرا اکبری",
        "email": "zahra.akbari@student.com",
        "phone": "09141234567"
    },
    {
        "name": "علی نوری",
        "email": "ali.noori@student.com",
        "phone": "09151234567"
    }
]

student_ids = []
for student in students:
    result = db["students"].insert_one(student)
    student_ids.append(str(result.inserted_id))
    print(f"   ✅ {student['name']} اضافه شد")

# ========================================
# 📕 دوره‌ها (5 دوره)
# ========================================
print("\n📚 اضافه کردن دوره‌ها...")

courses = [
    {
        "title": "آموزش پایتون از صفر تا صد",
        "description": "دوره جامع آموزش زبان برنامه‌نویسی پایتون برای مبتدیان",
        "instructor_id": instructor_ids[0],  # دکتر علی احمدی
        "price": 1500000
    },
    {
        "title": "هوش مصنوعی و یادگیری ماشین",
        "description": "آموزش الگوریتم‌های ML و کاربردهای واقعی AI",
        "instructor_id": instructor_ids[1],  # دکتر سارا محمدی
        "price": 2500000
    },
    {
        "title": "توسعه وب با React و FastAPI",
        "description": "ساخت برنامه‌های وب مدرن با React در فرانت‌اند و FastAPI در بک‌اند",
        "instructor_id": instructor_ids[2],  # مهندس رضا کریمی
        "price": 2000000
    },
    {
        "title": "تحلیل داده با Python",
        "description": "کار با Pandas، NumPy و Matplotlib برای تحلیل داده",
        "instructor_id": instructor_ids[3],  # دکتر مریم حسینی
        "price": 1800000
    },
    {
        "title": "معماری میکروسرویس",
        "description": "طراحی و پیاده‌سازی سیستم‌های توزیع‌شده با Docker و Kubernetes",
        "instructor_id": instructor_ids[4],  # مهندس حسین رضایی
        "price": 3000000
    }
]

course_ids = []
for course in courses:
    result = db["courses"].insert_one(course)
    course_ids.append(str(result.inserted_id))
    print(f"   ✅ {course['title']} اضافه شد")

# ========================================
# 📙 ثبت‌نام‌ها (5 ثبت‌نام)
# ========================================
print("\n📝 اضافه کردن ثبت‌نام‌ها...")

enrollments = [
    {
        "student_id": student_ids[0],  # محمد علیزاده
        "course_id": course_ids[0],     # آموزش پایتون
        "enrolled_at": "2024-01-15T10:30:00"
    },
    {
        "student_id": student_ids[1],  # فاطمه کاظمی
        "course_id": course_ids[1],     # هوش مصنوعی
        "enrolled_at": "2024-01-16T14:20:00"
    },
    {
        "student_id": student_ids[2],  # امیر حسین پور
        "course_id": course_ids[2],     # توسعه وب
        "enrolled_at": "2024-01-17T09:15:00"
    },
    {
        "student_id": student_ids[3],  # زهرا اکبری
        "course_id": course_ids[3],     # تحلیل داده
        "enrolled_at": "2024-01-18T11:45:00"
    },
    {
        "student_id": student_ids[4],  # علی نوری
        "course_id": course_ids[4],     # معماری میکروسرویس
        "enrolled_at": "2024-01-19T16:00:00"
    },
    # چند ثبت‌نام اضافی
    {
        "student_id": student_ids[0],  # محمد در دوره هوش مصنوعی هم ثبت‌نام کرده
        "course_id": course_ids[1],
        "enrolled_at": "2024-01-20T10:00:00"
    },
    {
        "student_id": student_ids[1],  # فاطمه در دوره پایتون هم ثبت‌نام کرده
        "course_id": course_ids[0],
        "enrolled_at": "2024-01-21T13:30:00"
    }
]

for enrollment in enrollments:
    result = db["enrollments"].insert_one(enrollment)
    print(f"   ✅ ثبت‌نام انجام شد")

# ========================================
# 📊 خلاصه
# ========================================
print("\n" + "="*50)
print("✅ تمام دیتاها با موفقیت اضافه شدند!")
print("="*50)
print(f"👨‍🏫 مدرس‌ها: {len(instructors)} نفر")
print(f"👨‍🎓 دانشجوها: {len(students)} نفر")
print(f"📚 دوره‌ها: {len(courses)} دوره")
print(f"📝 ثبت‌نام‌ها: {len(enrollments)} ثبت‌نام")
print("="*50)

# نمایش ID ها برای تست
print("\n📌 ID های ایجاد شده:")
print(f"\nاولین مدرس ID: {instructor_ids[0]}")
print(f"اولین دانشجو ID: {student_ids[0]}")
print(f"اولین دوره ID: {course_ids[0]}")

client.close()