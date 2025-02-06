from fastapi import APIRouter, Path,Depends,HTTPException,Query,status
from fastapi.responses import JSONResponse
from users.schemas import *
from users.models import UserModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List


router = APIRouter(tags=["users"],prefix="/users")


@router.post("/login")
async def user_login(request:UserLoginSchema,db:Session = Depends(get_db)):
    user_obj = db.query(UserModel).filter_by(username=request.username.lower()).first()
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="user doesnt exists")
    if not user_obj.verify_password(request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="password is invalid")
    
    return {}


@router.post("/register")
async def user_register(request:UserRegisterSchema,db:Session = Depends(get_db)):
    if db.query(UserModel).filter_by(username=request.username.lower()).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="username already exists")
    user_obj = UserModel(username=request.username.lower())
    user_obj.set_password(request.password)
    db.add(user_obj)
    db.commit()
    return JSONResponse(content={"detail":"user registered successfully"})