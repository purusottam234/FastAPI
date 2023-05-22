from enum import Enum
from fastapi import FastAPI,Path,Body
from pydantic import BaseModel

app = FastAPI()

class UserType(str,Enum):
    STANDARD = 'standard'
    ADMIN = 'admin'

@app.get('/users/{type}/{id}/')
async def get_user(type:UserType,id:int):
    return {'type':type,'id':id}  


@app.get('/users/{id}')
async def get_users(id:int = Path(...,ge=1)):
    return {'id':id}


@app.get('/license-plate/{license}')
async def get_license_plate(license:str = Path(..., min_length=9, max_length=9)):
    return {'license':license}


class User(BaseModel):
    name: str
    age: int

class Company(BaseModel):
    name:str 


# @app.post('/users')
# async def create_user(name:str = Body(...),age:int = Body(...)):
#     return {'name':name,'age':age}

# @app.post('/users')
# async def create_user(user:User,company:Company):
#     return  {'user':user,'company':company}

@app.post('/users')
async def create_user(user:User,priority: int = Body(...,ge=1, le=3)):
    return {'user':user,'priority':priority}