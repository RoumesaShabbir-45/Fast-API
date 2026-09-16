from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users= []

class User(BaseModel):
    name:str
    age:int

    #post api
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return{
        "message":"user created",
        "data":user
    }
#put api
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User,notify: bool = False):
  if user_id <len (users):
     users[user_id]=user
     return {
        "message":"user updated",
         "notify":notify,
        "data":user
        }
  return { 
   "error":"user not found"
}