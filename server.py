from fastapi import FastAPI

app=FastAPI()

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
@app.get("/ping")
def ping():
    return {"status": "ok"}

# 2. Dynamic Name Greeting (Path Parameter)
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Welcome to Rio Health, {name}!"}

