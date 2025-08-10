from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, EmailStr, Field
from fastapi import status
from fastapi import FastAPI

app = FastAPI()

reg_users = []
class userValidationModel(BaseModel):
    username:str
    password: constr(min_length=8)
    email: EmailStr | None = Field(default=None)



@app.post("/register")
def register(model: userValidationModel):
    reg_users.append(model.username)
    return f"{model.username} registered sucessfully"
    