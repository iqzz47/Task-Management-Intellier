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

from fastapi import APIRouter
from.import authenticationapi
from.import employeeapi
from.import taskapi

api = FastAPI()
api = FastAPI(title="Task management")

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api.include_router(authenticationapi.router, prefix="/api/auth", tags=["Authentication"])
api.include_router(employeeapi.user_router, prefix="/api/user", tags=["UserInfo"])
api.include_router(employeeapi.router, prefix="/api/user", tags=["UserInfo"])

api.include_router(taskapi.user_router, prefix="/api/task", tags=["Task"])




























"""

app = FastAPI()
app = FastAPI(title="Task management")


user_router = APIRouter()
router = APIRouter(dependencies=[Depends(get_current_user)])


items = {}
session = Session(engine) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()


@app.post("/createemployee",tags=["EMPLOYEE"]) 

def EmployeeCreate(user_data: Employee):
    user_crud_service = EmployeeCRUDService()
    new_user_instance = user_crud_service.createEmployee(user_data)
    
    return new_user_instance



@app.get("/readallemployee data",tags={"EMPLOYEE"})

def Employeeread():
    user_crud_service = EmployeeCRUDService()
    x = user_crud_service.getallEmployee(session= Depends(get_session))
    return x


@app.get("/readuserbyid",tags={"EMPLOYEE"})

def Employeereadbyid(employee_id:int):
    user_crud_service = EmployeeCRUDService()
    x=user_crud_service.getEmployeebyid(employee_id)
    return x
    


@app.put("/updateemployeedetail",tags={"EMPLOYEE"})

def EmployeeUpdate(employee_id:int,y:Employee):
        user_crud_service = EmployeeCRUDService()
        db_user_instance = user_crud_service.updateEmployee(employee_id, y)

        return db_user_instance


@app.delete("/deleteemployee",tags={"EMPLOYEE"})

def EmployeeDelete(employee_id:int):
     user_crud_service = EmployeeCRUDService()
     db_user_instance = user_crud_service.deleteEmployee(employee_id)

     return db_user_instance


@app.get("/verifyemployee",tags={"EMPLOYEE"})

def verify(employeeid:int):
     user_crud_service=EmployeeCRUDService() 
     db_user_instance = user_crud_service.verify(employeeid)
     return db_user_instance

@app.post("/createtask",tags={"Task"})

def TaskCreate(task_data: Task):
    new_task = Task(**task_data.dict())
    task_crud_service = TaskCRUDService()
    created_task = task_crud_service.createTask(new_task)
    return {"message": "Task created successfully", "task_details": created_task.dict()}
   
    

@app.get("/readalltask", tags={"Task"})

def Taskread():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getallTask(session= Depends(get_session))
    return x


@app.get("/readincompletetask",tags={"Task"})

def Taskreadincomplete():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getIncompleteTask(session= Depends(get_session))
    return x


@app.get("/readcompletetask",tags={"Task"})

def Taskreadincomplete():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getCompleteTask(session= Depends(get_session))
    return x


@app.get("/readonprogresstask",tags={"Task"})

def Taskreadonprogress():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getonprogressTask(session= Depends(get_session))
    return x

@app.get("/readcanceltask",tags={"Task"})

def Taskreadonprogress():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.cancelTask(session= Depends(get_session))
    return x


@app.get("/readtaskbyt_code/{t_code}", tags={"Task"})
def Taskreadbyid(t_code):
    print(f"Received t_code: {t_code}")
    user_crud_service = TaskCRUDService()
    x = user_crud_service.getTaskbyid(t_code)
    return x


@app.put("/updatetaskdetail/{t_code}",tags={"Task"})

def TaskUpdate(t_code:str,y:Task):
        print(f"Received t: {t_code}")
       
        user_crud_service = TaskCRUDService()
        db_task_instance = user_crud_service.updateTask(t_code, y)

        return db_task_instance

@app.delete("/deletetask",tags={"Task"})

def TaskDelete(t_code:str):
     user_crud_service = TaskCRUDService()
     db_user_instance = user_crud_service.deletetask(t_code)

     return db_user_instance


#Authentication API

@app.get("/token",tags={"Authentication"})
def AccessToken(employeeid:int,password:str):
    user_auth_service = AuthenticationService()
    x=user_auth_service.get_token(employeeid=employeeid,password=password)
    return x


    """