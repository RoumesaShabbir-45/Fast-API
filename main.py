from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,declarative_base,Session

app=FastAPI()

#database url
DATABASE_URL = "sqlite:///./Test.db"

#engin create database connection 
engine= create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread":False}
)
#session
SessionLocal =sessionmaker(bind=engine)

#base
Base = declarative_base()

#table model
class Todo(Base):
    __tablename__ ="todos"
   
    id= Column(Integer, primary_key=True, index=True)
    title= Column(String)
    completed= Column(String)


#table create
    Base.metadata.create_all(bind=engine)

#dependency
def get_db():
        db=SessionLocal()
        try:
            yield db
        finally:
            db.close()

#Create api
@app.post("/todos")
def create_todo(title:str, db: Session = Depends(get_db)):
    todo=Todo(title=title, completed="false")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "message":"Todo Created",
        "data": todo
    }

#read api
@app.get("/todos")
def get_todos(db: Session = Depends(get_db)):
     todos= db.query(Todo).all()
     return{
          "Total":len(todos),
          "data":todos
     }
#get data by id
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int, db: Session = Depends(get_db)):
     todo = db.query(Todo).filter(Todo.id==todo_id).first()
     if not todo:
          raise HTTPException(status_code=404,detail="todo not found")
     return todo

#update 
@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title=str, db: Session = Depends(get_db)):
     todo =db.query(Todo).filter(Todo.id==todo_id).first()
     if not todo:
              raise HTTPException(status_code=404,detail="todo not found") 
     todo.title= title
     db.commit()
     db.refresh(todo)

     return{
          "message":"todo updated",
          "data":todo
     }
#delete 
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int, db: Session = Depends(get_db)):
     todo =db.query(Todo).filter(Todo.id==todo_id).first()
     if not todo:
                   raise HTTPException(status_code=404,detail="todo not found") 
     db.delete(todo)
     db.commit()
     db.refresh(todo)
     return{
          "message":"todo deleted"
     }

