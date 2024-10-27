from fastapi import APIRouter, Depends, HTTPException
from src.apis.user.schemas import UserCreateSchema
router = APIRouter()


@router.post('/login')
async def login_user(username: str, password: str):
    return {"username": username, "password": password}

@router.post('/register')
async def login_user(user: UserCreateSchema):
    return {"username": user.username, "password": user.password}