from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from datetime import timedelta
from .model import Employee
from .security import *
from sqlmodel import Session,select,SQLModel, create_engine





class AuthenticationService:
    session = Session(engine)


     #before creating token verify user 
    def get_token(self, employeeid,password):
        emp = self.session.exec(select(Employee).where(Employee.id == employeeid)).first()        

        if not emp:
            return 0
            raise HTTPException(status_code=400, detail="ID is not registered")
        
        #if not verify_password(password, emp.password):
           # raise HTTPException(status_code=400, detail="Invalid login credential")
  
        token =get_user_token(emp)
        #y=get_token_user(token)

        return token


       

    
def get_user_token(employee:Employee):
    payload = {"id": employee.id}
    access_token_expiry = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))

    access_token = create_access_token(payload, access_token_expiry)
    return access_token
 
def get_token_user(token: str):
    payload = get_token_payload(token, SECRET_KEY, ALGORITHM)
 
    if payload:
        employeeid = payload.get('id')
        return employeeid
      

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_session)):
    user = get_token_user(token=token, db = db)
    if user:
        return user
    raise HTTPException(status_code=401, detail="Not authorised.")
    
