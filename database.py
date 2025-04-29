import json
from modules.user import UserRegister, User

def read_db():
    with open("data.json","r") as f:
        return json.load(f)

def save_db(data):
    with open("data.json", "w") as f:
        json.dump(obj=data,fp=f, indent=2)
        print("data updated")

def save_user_changes(user:User):
    data = read_db()
    data[user.username] = user.model_dump()
    save_db(data)

def get_user(username):
    data = read_db()
    return User(**data[username])

def add_new_user(user: UserRegister):
    data = read_db()
    data[user.username] = user.model_dump()
    save_db(data)

def check_user(username):
    data = read_db()
    if username not in data:
        return False
    return True
    

