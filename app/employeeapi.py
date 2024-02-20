from fastapi import FastAPI ,Depends,APIRouter

from .dbconfig import init_db
from sqlmodel import Session,select,SQLModel, create_engine
from fastapi.middleware.cors import CORSMiddleware
from .model import Employee
from .model import Task
from .employee_service import EmployeeCRUDService
from .task_service import TaskCRUDService
from .authentication_service import AuthenticationService
from fastapi import  Query
from .dbconfig import *
from .authentication_service import get_current_user





user_router = APIRouter()
router = APIRouter(dependencies=[Depends(get_current_user)])

@user_router.post("/createemployee",tags=["EMPLOYEE"]) 

def EmployeeCreate(user_data: Employee):
    user_crud_service = EmployeeCRUDService()
    new_user_instance = user_crud_service.createEmployee(user_data)
    
    return new_user_instance



@router.get("/readallemployee data",tags={"EMPLOYEE"})

def Employeeread():
    user_crud_service = EmployeeCRUDService()
    x = user_crud_service.getallEmployee(session= Depends(get_session))
    return x


@router.get("/readuserbyid",tags={"EMPLOYEE"})

def Employeereadbyid(employee_id:int):
    user_crud_service = EmployeeCRUDService()
    x=user_crud_service.getEmployeebyid(employee_id)
    return x
    


@router.put("/updateemployeedetail",tags={"EMPLOYEE"})

def EmployeeUpdate(employee_id:int,y:Employee):
        user_crud_service = EmployeeCRUDService()
        db_user_instance = user_crud_service.updateEmployee(employee_id, y)

        return db_user_instance


@router.delete("/deleteemployee",tags={"EMPLOYEE"})

def EmployeeDelete(employee_id:int):
     user_crud_service = EmployeeCRUDService()
     db_user_instance = user_crud_service.deleteEmployee(employee_id)

     return db_user_instance


@user_router.get("/verifyemployee",tags={"EMPLOYEE"})

def verify(employeeid:int):
     user_crud_service=EmployeeCRUDService() 
     db_user_instance = user_crud_service.verify(employeeid)
     return db_user_instance