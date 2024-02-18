from fastapi import Depends
from fastapi.security import APIKeyHeader
from passlib.context import CryptContext
from datetime import timedelta, datetime
from jose import jwt, JWTError
from .dbconfig import *




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = APIKeyHeader(name="access_token")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_token_payload(token: str, secret: str, algo: str):
    try:
        payload = jwt.decode(token, secret, algorithms=algo)
    except Exception as jwt_exec:
        payload = None
    return payload




