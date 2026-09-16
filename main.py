from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str
# #Users
# @app.post("/create_users")
# def create_user(user:User):
#     return{
#         "message":"user created",
#         "data":user
#            }

class Address(BaseModel):
    city:str
    pincode:int

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/created_user")
def created_user(user:User):
    return{
        user
    }