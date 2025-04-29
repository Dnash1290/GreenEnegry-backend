from pydantic import BaseModel
from typing import Optional, List
from modules.booking import Booking


class UserLogin(BaseModel):
    username:str 
    password:str

class UserRegister(UserLogin):
    name:str
    surname:str

class UserChangePassword(UserLogin):
    surname:str

class User(UserRegister):
    booking:Optional[List[Booking]] = []
