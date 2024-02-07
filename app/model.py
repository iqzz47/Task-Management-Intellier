from sqlmodel import SQLModel, Field, String, Boolean
from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class Employee(SQLModel ,table=True):
    __tablename__ = 'Employee' 
    id: int | None = Field(primary_key=True, index=True)
    firstName: str | None = Field(nullable=False)
    lastName: str | None = Field(nullable=False)
    emailAddress: str | None = Field(nullable=False)
    phoneNo: str | None = Field(nullable=False)
    designation:str|None = Field(nullable=False)
    department:str|None = Field(nullable=False)
    linemanager:int|None=Field(nullable=True)

class Task(SQLModel, table=True):
    __tablename__ = 'Task' 
    
    t_code: str | None = Field(primary_key=True, index=True)
    taskname:str | None = Field(nullable=True)
    createdate:datetime | None = Field(nullable=True)
    duedate:datetime | None = Field(nullable=True)
    duration:str | None = Field(nullable=True)
    status:str| None = Field(default="Incomplete")
    assignedfrom: int | None = Field(foreign_key="Employee.id")
    assignedto:int | None = Field(foreign_key="Employee.id")


    

    
   
  