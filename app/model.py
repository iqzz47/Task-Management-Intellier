from sqlmodel import SQLModel, Field, String, Boolean
from datetime import datetime

class Employee(SQLModel ,table=True):
    
    id: int | None = Field(primary_key=True, index=True)
    firstName: str | None = Field(nullable=True)
    lastName: str | None = Field(nullable=True)
    emailAddress: str | None = Field(nullable=True)
    phoneNo: str | None = Field(nullable=True)
    designation:str|None = Field(nullable=True)
    department:str|None = Field(nullable=True)
    linemanager:str|None=Field(nullable=True)


class Task(SQLModel, table=True):
    
    t_code: str | None = Field(primary_key=True, index=True)
    taskname:str | None = Field(nullable=True)
    createdate:datetime | None = Field(nullable=True)
    duedate:datetime | None = Field(nullable=True)
    duration:str | None = Field(nullable=True)
    status:str| None = Field(nullable=True)
    assignedfrom:str | None = Field(nullable=True)
    assignedto:str | None = Field(nullable=True)

    

    
   
  