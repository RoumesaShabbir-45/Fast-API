from fastapi import FastAPI, status, HTTPException


app = FastAPI()

@app.post("/created_user",status_code= status.HTTP_201_CREATED)
def create_user():
 return{
  "message":"user created"
 }

#custom response
@app.get("/user")
def get_users():
  return{
    "ststus":"success",
    "message":"userFetched",
    "data":{
      "name":"mohit",
      "age": 24
    }
  }
#basic error handler
@app.get("/users/{user_id}")
def get_user(user_id:int):
  if user_id !=1:
    raise HTTPException(
      status_code= 404,
      detail="user not found"
    )
  return{
    "id":"1",
    "name":"mohit"
  }
