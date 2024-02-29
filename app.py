from fastapi import FastAPI
import sql_quries

app = FastAPI()

@app.get("/get-all-users")
def get_all_users():
    return sql_quries.get_all_users()

@app.post("/add-user")
def add_user(name: str, email: str, password: str):
    return sql_quries.add_user(name, email, password)