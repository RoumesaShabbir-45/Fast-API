from fastapi import FastAPI,HTTPException,Depends
from jose import jwt
from datetime import datetime,timezone,timedelta
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from passlib.context import CryptContext


app=FastAPI()
#jwt config
SECREAT_KEY= "mysecreat"
ALGORITHM="HS256"
Access_token_Expiary_Minuts=30

#password hashing setup
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

#OAuth setup
oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")

#dummy user db
fake_user_db={
    "admin":{
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}

#hashing password
def hash_password(password:str):
    return pwd_context.hash(password[:72])

#verify password
def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password[:72],hashed_password)

#create token function
def create_token(data:dict):
    to_encode=data.copy()
    expire= datetime.now(timezone.utc)+timedelta(minutes=30)
    to_encode.update({
      "exp":expire
})

    token=jwt.encode(to_encode,SECREAT_KEY,algorithm=ALGORITHM)
    return token

#login api(OAuth2 form)
@app.post("/login")
def login(form_data:OAuth2PasswordRequestForm = Depends()):
    user=fake_user_db.get(form_data.username)
    if not user or not verify_password(form_data.password,user["hashed_password"]):
      raise HTTPException(
        status_code=400,
        detail="invalid usernmae and password"
    )
    access_token=create_token({
       "sub":form_data.username
    })
    return{
       "access_token":access_token,
       "token_type":"bearer"
    }
#verify token
def varify_token(token: str = Depends(oauth2_schema)):
    try:
        payload=jwt.decode(token,SECREAT_KEY,algorithms=[ALGORITHM])
        username:str=payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="invalid or expire token"
            )
        
        return username
    except jwt.JWTError:
        raise HTTPException(
        status_code=401,
        detail="invalid token"
        )

#protected routes
@app.get("/protected")
def protected_routes(username:str =Depends(varify_token)):
    return{
        "message":"secure data accessed",
        "user":username
    }

        