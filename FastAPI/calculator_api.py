from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/calculator")
def calculator():
    return "Please use the route Add,Substract,Multiple,Divide for calculation"

class calcValidationModel(BaseModel):
    a:int
    b:int

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b== 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    else:
        return a / b

@app.post("/calculator/addition")
def addition(model: calcValidationModel):
    return add(model.a,model.b)

@app.post("/calculator/substraction")
def substraction(model: calcValidationModel):
    return subtract(model.a,model.b)

@app.post("/calculator/mutiplication")
def mutiplication(model: calcValidationModel):
    return multiply(model.a,model.b)

@app.post("/calculator/division")
def division(model: calcValidationModel):
    return divide(model.a,model.b)