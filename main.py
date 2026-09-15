from fastapi import FastAPI

app = FastAPI()
#home
@app.get("/")
def home():
    return{"message":"Hello fastapi with vern"}

#About
@app.get("/about")
def about():
    return{"message":"this is about page"}

#Users
@app.get("/users")
def users():
    return{
        "users":["Ahmad","Roumesa","Hamza"]
    }