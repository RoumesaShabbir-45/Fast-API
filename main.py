from fastapi import FastAPI

app = FastAPI()
#Users
@app.post("/create_users")
def create_user(user:dict):
    return{
        "message":"user created",
        "data":user
           }


