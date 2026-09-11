from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"message": "hello guysss welcome to rio_health"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

# 2. Dynamic Name Greeting (Path Parameter)
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Welcome to Rio Health, {name}!"}