from sqlmodel import Session,select
from .model import Employee,Task
from sqlmodel import Session, SQLModel, create_engine

from .dbconfig import *
class EmployeeCRUDService:
   


    session = Session(engine)

    def createEmployee(self, new_employee: Employee):
        #print("here employee will be created")
        new_employee_instance = Employee.from_orm(new_employee)
        self.session.add(new_employee_instance)
        self.session.commit()
        self.session.refresh(new_employee_instance)

        return new_employee_instance

    def getallEmployee(self,session=session):
        users = self.session.exec(select(Employee)).all()
        return users

    def getEmployeebyid(self,employee_id):
        user = self.session.exec(select(Employee).where(Employee.id == employee_id)).one_or_none()
        return user
    

    

    def updateEmployee(self, employee_id: int, updated_employee: Employee):
       
            existing_employee = self.session.exec(select(Employee).where(Employee.id == employee_id)).one_or_none()

            if existing_employee:
           
                    for key, value in updated_employee.dict().items():
                        setattr(existing_employee, key, value)

           
                    self.session.commit()
                    self.session.refresh(existing_employee)

                    return existing_employee
            else:
          
                    return None

    def deleteEmployee(self,Employeeid):
          user_to_delete = self.getEmployeebyid(employee_id=Employeeid)
          self.session.delete(user_to_delete)
          self.session.commit()

          return True

        
            


    

    
