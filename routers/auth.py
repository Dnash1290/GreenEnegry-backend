from fastapi import APIRouter
from modules.user import * 
from database import *
from fastapi import HTTPException
auth_router = APIRouter()

@auth_router.post("/register")
def register(user:UserRegister):
    if check_user(user.username):
        print("print username in use")
        raise HTTPException(status_code=403, detail="this username is in user")
    
    add_new_user(user)
    return {"message":"the user account has been added"}


@auth_router.post("/login")
def login(userlog:UserLogin):
    if not check_user(userlog.username):
        raise HTTPException(status_code=404, detail="username or password is invalid")
    user = get_user(userlog.username)
    if userlog.password != user.password:
        raise HTTPException(status_code=404, detail="username or password is invalid")
    return user

@auth_router.put("/forgotpassword")
def change_password(userlog:UserChangePassword):
    if not check_user(userlog.username):
        raise HTTPException(status_code=422, detail="details are invalid")
    user = get_user(userlog.username)

    if user.surname != userlog.surname:
        raise HTTPException(status_code=422, detail="details are invalid")
    
    user.password = userlog.password
    save_user_changes(user)
    return {"message":"password changed"}
