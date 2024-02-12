from fastapi import FastAPI ,Depends
from .dbconfig import init_db
from sqlmodel import Session,select,SQLModel, create_engine
from fastapi.middleware.cors import CORSMiddleware
from .model import Employee
from .model import Task
from .employee_service import EmployeeCRUDService
from .task_service import TaskCRUDService
from fastapi import  Query
from .dbconfig import *

app = FastAPI()
app = FastAPI(title="Task management")


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



@app.get("/readtaskbyt_code/{t_code}", tags={"Task"})
def Taskreadbyid(t_code):
    print(f"Received t_code: {t_code}")
    user_crud_service = TaskCRUDService()
    x = user_crud_service.getTaskbyid(t_code)
    return x


@app.put("/updatetaskdetail/{t_code}",tags={"Task"})

def TaskUpdate(t_code:str,y:Task):
        print(f"Received t_code: {t_code}")
        print(f"Received t_code: {Task.duration}")
        user_crud_service = TaskCRUDService()
        db_task_instance = user_crud_service.updateTask(t_code, y)

        return db_task_instance

@app.delete("/deletetask",tags={"Task"})

def TaskDelete(t_code:str):
     user_crud_service = TaskCRUDService()
     db_user_instance = user_crud_service.deletetask(t_code)

     return db_user_instance