from fastapi import FastAPI, Depends,Header, HTTPException

app=FastAPI()

#auth to handle token
def varify_token(token:str = Header(None)):
 if token != "myscreatkey": 
  raise HTTPException(
   status_code=401,
   detail="Unauthorized"
  )
 return{
  "user":"authorized user"
 }
@app.get("/secure_data")
def secure_data(user=Depends(varify_token)):
 return{
  "message":"secure data accessed",
  "user":user
 }

#reuseable logic
# def get_current_user():
#     return{
#         "user":"mohit"
#     }
# @app.get("/profile")
# def profile(user= Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def dashboard(user= Depends(get_current_user)):
#     return user
  

#Depends logic
# def common_logic():
#     return{
#         "meassage":"common logic executed"
#     }
# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data