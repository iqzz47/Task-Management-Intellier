import psycopg2
import json
from .dbconfig import conn,cursor
from fastapi import HTTPException

class User:
    def __init__(self, db_name, user, password):
        self.conn = psycopg2.connect(f"dbname={db_name} user={user} password={password}")
        self.cursor = self.conn.cursor()

    def create_user(self, user_data:dict):
      
        user_dict = json.loads(user_data)
      
       
        user_query = "SELECT name FROM users WHERE email = %s;"
        self.cursor.execute(user_query, (user_dict['email'],))
        existing_user = self.cursor.fetchone()
        
       
        
        
        if existing_user:
            raise HTTPException(status_code=404,detail="User cannot be created email exist")
        
        user_query = "SELECT name FROM users WHERE phone = %s;"
        self.cursor.execute(user_query, (str(user_dict['phone']),))
        existing_user = self.cursor.fetchone()


        if existing_user:
            raise HTTPException(status_code=404,detail="User cannot be created phone number exist")
        else:
             sql = "INSERT INTO users (name, phone, email, city, country) VALUES (%s, %s, %s, %s, %s);"
             values = (user_dict['name'], user_dict['phone'], user_dict['email'], user_dict['city'], user_dict['country'])
             self.cursor.execute(sql, values)
             self.conn.commit()
            



       
        
       
    def read_user(self, user_id):
       
        try:
            sql = "SELECT * FROM users WHERE id = %s;"
            self.cursor.execute(sql, (user_id,))
            
            user_data = self.cursor.fetchone()
            return user_data
            #print(f"User Data: {user_data}")
        except Exception as e:
            print(f"Error reading user: {e}")
    
    
    def read_all_users(self) -> list:
          try:
            sql = "SELECT * FROM users;"
            self.cursor.execute(sql)
            all_users = self.cursor.fetchall()
            return all_users
          
          except Exception as e:
            print(f"Error reading all users: {e}")
            return []
          
    def update_user(self, user_id, new_user_data: dict):
        new_user_data = json.loads(new_user_data)
        try:
            sql = "UPDATE users SET name = %s, phone = %s, email = %s, city = %s, country = %s WHERE id = %s;"
            values = (new_user_data['name'], new_user_data['phone'], new_user_data['email'], new_user_data['city'], new_user_data['country'], user_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print(f"User with ID {user_id} has been updated successfully.")
        except Exception as e:
            print(f"Error updating user: {e}")


    def delete_user(self, user_id):
        try:
            sql = "DELETE FROM users WHERE id = %s;"
            self.cursor.execute(sql, (user_id,))
            self.conn.commit()
            return(f"User with ID {user_id} has been deleted successfully.")
        except Exception as e:
            return(f"Error deleting user: {e}")

    def close_connection(self):
        self.conn.close()

"""
user_ops = User(db_name="testdb", user="postgres", password="admin")
user_ops.create_user('{"name": "New User", "phone": "123456789", "email": "newuser@example.com", "city": "City", "country": "Country"}')
user_ops.read_user(1)




#user_ops.delete_user(15)
all_users = user_ops.read_all_users()
print("All Users:")

for user in all_users:
    print(user)
user_ops.close_connection()

          
"""
