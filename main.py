from fastapi import FastAPI,Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

app=FastAPI()

#limiter setup
Limiter = Limiter(key_func=get_remote_address)

app.state.limiter = Limiter

#error handle
@app.exception_handler(RateLimitExceeded)
def rate_limit_hander(request:Request, exc:RateLimitExceeded):

    return JSONResponse(
        status_code=429,
        content={
            "detail":"to many requests"
        }
    )
 #rate limit api
@app.get("/data")
@Limiter.limit("5/minute")
def get_data(request:Request):
    return{
        "message":"Success"
    }
