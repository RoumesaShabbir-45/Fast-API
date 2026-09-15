from fastapi import FastAPI

app = FastAPI()
#Users
@app.get("/users")
def get_user(name: str=None):
    return{"Name": name}

#Default value
@app.get("/products")
def get_user(limit: int=10):
    return{"limit": limit}

#Mulitiquery parmas
@app.get("/items")
def get_user(name: str=None , price: int=10):
    return{"name": name,
          "price": price
          }

