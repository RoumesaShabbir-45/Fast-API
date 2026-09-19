from fastapi import FastAPI,HTTPException,Header,Depends
from jose import jwt
from datetime import datetime,timezone,timedelta

app=FastAPI()
#making secure key
SECREAT_KEY= "mysecreat"
ALGORITHM="HS256"

#create token function
def create_token(data:dict):
    to_encode=data.copy()
    expire= datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
      "exp":expire
})

    token=jwt.encode(to_encode,SECREAT_KEY,algorithm=ALGORITHM)
    return token

#login api(token generate)
@app.post("/login")
def login(username:str ,password:str):
    if username!="admin" or password!="123456":
      raise HTTPException(
        status_code=401,
        detail="invalid usernmae and password"
    )
    token=create_token({
       "sub":username
    })
    return{
       "access_token":token
    }
#verify token
def varify_token(token: str = Header(None)):

    try:
        payload=jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(
        status_code=401,
        detail="invalid or expire token"
        )
#protected routes
@app.get("/secure")
def secure_data(user=Depends(varify_token)):
    return{
        "message":"secure data accessed",
        "user":user
    }

        