from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

app = FastAPI()

## JWT configuration
secret_key = "enrypted_key"
ALGORITHM = "HS256"
token_expire_minutes = 30

#hashing password setup
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#auth setup
auth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
#create token
def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({"exp": expire})

#encode the token
    token=jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    return token

#verify token
def verify_token(token: str = Depends(auth2_scheme)):
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
        
    
    
    