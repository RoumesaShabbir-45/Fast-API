from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int
#Users
@app.post("/create_users")
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
           }


