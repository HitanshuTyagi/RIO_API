from fastapi import FastAPI

app = FastAPI()

students = [
    {"id": 1, "name": "Gourav", "course": "CSE", "year": 4},
    {"id": 2, "name": "Rahul", "course": "ECE", "year": 3},
    {"id": 3, "name": "Ankit", "course": "CSE", "year": 4}
]


students = [
    {"id": 1, "name": "Gourav", "course": "CSE", "year": 4},
    {"id": 2, "name": "Rahul", "course": "ECE", "year": 3},
]

@app.get("/")
def home():
    return {"message": "hello guysss welcome to rio_health"}



@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ]

    user = next((u for u in users if u["id"] == user_id), None)
    return user


@app.get("/students")
def students_data():
    return students


@app.get("/student/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student_id == student["id"]:
            return student

    return {"message": "Student not found"}


@app.get('/students')
def students_data():
    return students

@app.get('/student/{student_id}')
def get_student(student_id:int):
    for student in students:
        if student_id==student.id:
            return student

    return {"message":"Student not found in the database"}

@app.get("/ping")
def ping():
    return {"status": "ok"}


@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Welcome to Rio Health, {name}!"}

print("main commit")
print("practice commit 1")
