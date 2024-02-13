from sqlmodel import Session, create_engine,select
from .model import Employee, Task
from .dbconfig import *


class TaskCRUDService:

    session = Session(engine)
    def createTask(self, new_Task: Task):
        new_task_instance = Task.from_orm(new_Task)
        self.session.add(new_task_instance)
        self.session.commit()
        self.session.refresh(new_task_instance)
        return new_task_instance
 

    def getallTask(self, session=session):
        tasks = self.session.exec(select(Task)).all()
        return tasks
    
    def getIncompleteTask(self, session=session):
        tasks = self.session.exec(select(Task).where(Task.status == "Incomplete")).all()
        return tasks
    
    def getCompleteTask(self, session=session):
        tasks = self.session.exec(select(Task).where(Task.status == "Complete")).all()
        return tasks
    
    def getonprogressTask(self, session=session):
        tasks = self.session.exec(select(Task).where(Task.status == "On Progress")).all()
        return tasks

    def getTaskbyid(self,t_code):
        user = self.session.exec(select(Task).where(Task.t_code == t_code)).one_or_none()
        return user
    
    def cancelTask(self,session=session):
         tasks = self.session.exec(select(Task).where(Task.status == "Cancel")).all()
         return tasks


    def updateTask(self, t_code:str, updated_task: Task):
       
            existing_task = self.session.exec(select(Task).where(Task.t_code == t_code)).one_or_none()

            if existing_task:
           
                    for key, value in updated_task.dict().items():
                        setattr(existing_task, key, value)

           
                    self.session.commit()
                    self.session.refresh(existing_task)

                    return existing_task
            else:
          
                    return None

    def deletetask(self,t_code):
          task_to_delete = self.getTaskbyid(t_code=t_code)
          self.session.delete(task_to_delete)
          self.session.commit()

          return True

          
        

    
