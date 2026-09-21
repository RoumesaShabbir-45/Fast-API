from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app= FastAPI()

#allowed origins(frontend_url)
Origins = [
     "http://localhost:3000"
]

app.add_middleware (
    CORSMiddleware,
    allow_origins= Origins,
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def home():
    return{
        "message":"CORS Enable API"
    }