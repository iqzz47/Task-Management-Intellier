from pydantic import BaseModel

class ProductCreate(BaseModel):
    
    name: str
    price: int


class UserCreate(BaseModel):
    
    name: str
    phone: str
    email:str
    city:str
    country:str

class OrderCreate(BaseModel):
    
    user_id:int
    product_id:int
    quantity:int