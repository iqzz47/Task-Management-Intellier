from fastapi import APIRouter, Depends, status, Header
from sqlmodel import Session
from .dbconfig import get_session
from .authentication_service import AuthenticationService



router = APIRouter()

@router.get("/token",tags={"Authentication"},status_code=status.HTTP_200_OK)
def AccessToken(employeeid:int,password:str):
    user_auth_service = AuthenticationService()
    x=user_auth_service.get_token(employeeid=employeeid,password=password)
    return x


