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


@user_router.post("/createtask",tags={"Task"})

def TaskCreate(task_data: Task):
    new_task = Task(**task_data.dict())
    task_crud_service = TaskCRUDService()
    created_task = task_crud_service.createTask(new_task)
    return {"message": "Task created successfully", "task_details": created_task.dict()}
   
    

@user_router.get("/readalltask", tags={"Task"})

def Taskread():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getallTask(session= Depends(get_session))
    return x


@user_router.get("/readincompletetask",tags={"Task"})

def Taskreadincomplete():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getIncompleteTask(session= Depends(get_session))
    return x


@user_router.get("/readcompletetask",tags={"Task"})

def Taskreadincomplete():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getCompleteTask(session= Depends(get_session))
    return x


@user_router.get("/readonprogresstask",tags={"Task"})

def Taskreadonprogress():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.getonprogressTask(session= Depends(get_session))
    return x

@user_router.get("/readcanceltask",tags={"Task"})

def Taskreadonprogress():
    task_crud_service = TaskCRUDService()
    x = task_crud_service.cancelTask(session= Depends(get_session))
    return x


@user_router.get("/readtaskbyt_code/{t_code}", tags={"Task"})
def Taskreadbyid(t_code):
    print(f"Received t_code: {t_code}")
    user_crud_service = TaskCRUDService()
    x = user_crud_service.getTaskbyid(t_code)
    return x


@user_router.put("/updatetaskdetail/{t_code}",tags={"Task"})

def TaskUpdate(t_code:str,y:Task):
        print(f"Received t: {t_code}")
       
        user_crud_service = TaskCRUDService()
        db_task_instance = user_crud_service.updateTask(t_code, y)
        return db_task_instance

@user_router.delete("/deletetask",tags={"Task"})

def TaskDelete(t_code:str):
     user_crud_service = TaskCRUDService()
     db_user_instance = user_crud_service.deletetask(t_code)
     return db_user_instance


