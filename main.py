from fastapi import FastAPI,Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine,SessionLocal
from auth import create_token, verify_token
import models,schemas

app = FastAPI()
#db dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(bind=engine)

#login route
@app.post("/login")
def login():
    return {
        "access_token": create_token({"user": "admin"}),
        "token_type": "bearer"
    }
    
#home route
@app.get("/")
def home():
    return {"message": "Welcome!"}

#create user route(protected)
@app.post("/users/")
def create_user(user: schemas.Usercreate, db: Session = Depends(get_db), _ = Depends(verify_token)):
    db_user = models.User(
        title=user.title,
        username=user.username,
        email=user.email,
        hashed_password=user.password
    )
    db.add(db_user) 
    db.commit()
    db.refresh(db_user)
    return {
        "message": "User created successfully",
        "data": db_user
    }
#read user by id route
@app.get("/users/{id}", response_model=schemas.Userresponse)
def get_user(id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

#read users route
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    db_users = db.query(models.User).all()
    return db_users

#update user route
@app.put("/users/{id}")
def update_user(id: int, user: schemas.Usercreate, db: Session = Depends(get_db),_ = Depends(verify_token)):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.title = user.title
    db_user.username = user.username
    db_user.email = user.email
    db_user.hashed_password = user.password
    db.commit()
    db.refresh(db_user)
    return {
        "message": "User updated successfully",
        "data": db_user
    }
#delete user route(protected)
@app.delete("/users/{id}")
def delete_user(id:int, db: Session = Depends(get_db), _ = Depends(verify_token)):
    db_user = db.query(models.User).filter(models.User.id == id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {
        "message": "User deleted successfully"
    }
