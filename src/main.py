from fastapi import FastAPI
from .product import Product
from .user import User
from .order import Order
from .schema import ProductCreate
from .schema import UserCreate
from .schema import OrderCreate
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI(title="Test")


origins = [
   
    "http://localhost",
   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



#User crud operation
@app.get("/get_user",tags=["User"])
def read_user():
    user_ops = User(db_name="testdb", user="postgres", password="admin")
    all_users = user_ops.read_all_users()
    return all_users


@app.get("/get_user by id",tags=["User"])
def read_user(id):
    user_ops = User(db_name="testdb", user="postgres", password="admin")
    all_users = user_ops.read_user(id)
    return all_users

@app.post("/create_user",tags=["User"])
def create_user(p_schema:UserCreate):
    user_ops = User(db_name="testdb", user="postgres", password="admin")
    x= {"name":p_schema.name,"phone":p_schema.phone,"email":p_schema.email,"city":p_schema.city,"country":p_schema.country}
    y=json.dumps(x)
    user_ops.create_user(y)


    return {"message": "User created successfully"}


@app.put("/update_user",tags=["User"])
def update_user(id,p_schema:UserCreate):
    user_ops = User(db_name="testdb", user="postgres", password="admin")
    x= {"name":p_schema.name,"phone":p_schema.phone,"email":p_schema.email,"city":p_schema.city,"country":p_schema.country}
    y=json.dumps(x)
    user_ops.update_user(id,y)
    return {"message": "User updated successfully"}

@app.delete("/delete_user",tags=["User"])
def delete_product(id:int):
     user_ops = User(db_name="testdb", user="postgres", password="admin")
     x=user_ops.delete_user(id)
     return{"message":x}

#Product crud operation



@app.get("/get_product",tags=["product"])
def read_product():
    product_ops = Product(db_name="testdb", user="postgres", password="admin")
    all_products = product_ops.read_all_products()
    return all_products


@app.post("/create_product",tags=["product"])
def create_product(p_schema:ProductCreate):
    user_ops = Product(db_name="testdb", user="postgres", password="admin")
    x= {"name":p_schema.name,"price":p_schema.price}
    y=json.dumps(x)
    user_ops.create_product(y)


    return {"message": "Product created successfully"}




@app.put("/update_product",tags=["product"])
def update_product(id:int,p_schema:ProductCreate):
    user_ops = Product(db_name="testdb", user="postgres", password="admin")
    x= {"name":p_schema.name,"price":p_schema.price}
    y=json.dumps(x)
    z=user_ops.update_product(id,y)
    return {"message": z}

@app.delete("/delete_product",tags=["product"])

def delete_product(id:int):
     user_ops = Product(db_name="testdb", user="postgres", password="admin")
     user_ops.delete_product(id)
     return{"message":"Product deleted"}

     
#Order crud operation


@app.get("/get_order",tags=["Order"])
def read_user():
    user_ops = Order(db_name="testdb", user="postgres", password="admin")
    all_users = user_ops.read_all_orders()
    return all_users

@app.post("/create_order",tags=["Order"])
def create_order(p_schema:OrderCreate):
    user_ops = Order(db_name="testdb", user="postgres", password="admin")
    x= {"user_id":p_schema.user_id,"product_id":p_schema.product_id,"quantity":p_schema.quantity}
    y=json.dumps(x)
    user_ops.create_order(y)


    return {"message": "Order created successfully"}


@app.put("/update_order",tags=["Order"])
def update_order(id,p_schema:OrderCreate):
    user_ops = Order(db_name="testdb", user="postgres", password="admin")
    x= {"user_id":p_schema.user_id,"product_id":p_schema.product_id,"quantity":p_schema.quantity}
    y=json.dumps(x)
    user_ops.update_order(id,y)
    return {"message": "Order updated successfully"}

@app.delete("/delete_order",tags=["Order"])
def delete_order(id:int):
     user_ops = Order(db_name="testdb", user="postgres", password="admin")
     x=user_ops.delete_order(id)
     return{"message":x}