from fastapi import FastAPI
from pydantic import BaseModel   #data validation


#uvicorn test:app --reload


#put - to update
#delete - to delete a record
app = FastAPI()

user_db = {
    1:{"name":"Dhinesh","age":30},
    2:{"name":"DAPS","age":25},
    3:{"name":"Fetquest","age":20}
}

@app.get("/")
def add(a:int,b:int):   #by using :int data type will be used
    return a+b

@app.get("/daps/add")
def add(a:int,b:int):   #by using :int data type will be used
    return a+b


class subtractmodel(BaseModel):   # for validation - required for the post
    a:int
    b:int

class multiplication(BaseModel):   # for validation - required for the post
    a:int
    b:int

def substract(a:int,b:int):
    return a-b

def multi(a:int,b:int):
    return a*b

@app.post("/subtract")
def sub_nums(model: subtractmodel):
    return substract(model.a, model.b)

@app.post("/multiply")
def multiply(model:multiplication):    #FastAPI takes the raw JSON body → {"a": "3", "b": 4}  a must be an int → "3" can be coerced to 3  model = multiplication(a=3, b=4)_     
    return multi(model.a, model.b)

class User(BaseModel):
    name:str
    age:int

@app.put("/user_db/data/v1/update/{user_id}")   #route should have the parameter
def user_update(user_id:int,user:User):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        return {"message":"user updated for", "user":user_db[user_id]}
    else:
        return {"message":"user not found"}
    
@app.delete("/user_db/data/v1/delete/{user_id}")
def delete_user(user_id:int):
    if user_id in user_db:
        del user_db[user_id]
        return {"message":"user deleted"}
    else:
        return {"message":"user not found"}

#http://localhost:8000/docs
#http://127.0.0.1:8000/daps/add?a=4&b=5

#GET - data is visible in url header - non secured
#POST - data will be in body and not visible - secured