from fastapi import APIRouter
from.import authenticationapi
from.import employeeapi
from.import taskapi

api = APIRouter()

api.include_router(authenticationapi.router, prefix="/api/auth", tags=["Authentication"])
api.include_router(employeeapi.user_router, prefix="/api/user", tags=["UserInfo"])
api.include_router(employeeapi.router, prefix="/api/user", tags=["UserInfo"])
