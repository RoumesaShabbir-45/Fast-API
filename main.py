from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []
class Todo(BaseModel):
    id: int
    title: str
    completed: bool


    #create api
@app.post("/todos")
def create_todo(todo: Todo):
        todos.append(todo)
        return {
            "message":"TODO added",
            "data":todo
        }
  #read api
@app.get("/todos")
def get_todos():
        return {
           "todos": todos
        }
    #single data fetch (path params)
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
        for todo in todos:
            return
        {"error":"Todo not Found"}

    #update api
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
        for index, todo in enumerate(todos):
            if todo.id == todo_id:
                todos[index] = updated_todo
                return {
                    "message":"data updated",
                    "data":updated_todo
                }
            return {"error":"Todo not Found"}

     #delete api
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
             for index, todo in enumerate(todos):
                 if todo.id == todo_id:
                     todos.pop(index)
                     return {"message":"data deleted"}
                 return {"error":"Todo not Found"}

            
    

    
