from pydantic import BaseModel

class Usercreate(BaseModel):
    title: str
    username: str
    email: str
    password: str

class Userresponse(BaseModel):
    id: int
    title: str
    username: str
    email: str

    class Config:
        from_attributes = True



