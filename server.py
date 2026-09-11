from fastapi import FastAPI

app=FastAPI()

students = [
    {"id": 1, "name": "Gourav", "course": "CSE", "year": 4},
    {"id": 2, "name": "Rahul", "course": "ECE", "year": 3},
    {"id": 3, "name": "Ankit", "course": "CSE", "year": 4}
]

@app.get("/")
def home():
    return {"message": "hello guysss welcome to rio_health"}


@app.get('/students')
def students_data():
    return students

@app.get('/student/{student_id}')
def get_student(student_id:int):
    for student in students:
        if student_id==student.id:
            return student

    return {"message":"Student not found"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

# 2. Dynamic Name Greeting (Path Parameter)
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Welcome to Rio Health, {name}!"}
