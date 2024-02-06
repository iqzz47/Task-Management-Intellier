import psycopg2
import json
from .dbconfig import conn,cursor
class Product:
    def __init__(self, db_name, user, password):
        self.conn = psycopg2.connect(f"dbname={db_name} user={user} password={password}")
        self.cursor = self.conn.cursor()

    def create_product(self, product_data:dict):
      
        product_dict = json.loads(product_data)

       
        # proper error handling here
        try:
            sql = "INSERT INTO product (name, price) VALUES (%s, %s);"
            print(type(product_data))
            values = (product_dict['name'], product_dict['price'])
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Product has been inserted successfully.")
        except Exception as e:
            print(f"Error inserting user: {e}")
    
    def read_product(self, user_id):
       
        try:
            sql = "SELECT * FROM product WHERE id = %s;"
            self.cursor.execute(sql, (user_id,))
            
            user_data = self.cursor.fetchone()
            print(f"User Data: {user_data}")
        except Exception as e:
            print(f"Error reading user: {e}")
    
    
    def read_all_products(self) -> list:
          try:
            sql = "SELECT * FROM product;"
            self.cursor.execute(sql)
            all_users = self.cursor.fetchall()
            return all_users
          
          except Exception as e:
            print(f"Error reading all users: {e}")
            return []
          
    def update_product(self, product_id:int, new_product_data: dict):
        product_dict = json.loads(new_product_data)
        try:
            print("hello")
            print(new_product_data)
            print(product_id)
            print(type( product_dict ))
            sql="""UPDATE product SET name = '{0}', price = '{1}' WHERE id = {2};""".format( product_dict ['name'],  product_dict ['price'], int(product_id))
            #print(sql)

            
            self.cursor.execute(sql)
            self.conn.commit()
            #print(f"User with ID {product_id} has been updated successfully.")"""
        except Exception as e:
            print(f"Error updating user:  {e}")


    def delete_product(self, product_id):
        try:
            sql = "DELETE FROM product WHERE id = %s;"
            self.cursor.execute(sql, (product_id,))
            self.conn.commit()
            print(f"User with ID {product_id} has been deleted successfully.")
        except Exception as e:
            print(f"Error deleting user: {e}")

    def close_connection(self):
        self.conn.close()

"""
product_ops = Product(db_name="testdb", user="postgres", password="admin")
product_ops.create_product('{"name": "Bread", "price": "20"}')
product_ops.read_product(1)




product_ops.delete_product(3)
all_products = product_ops.read_all_products()
print("All Products:")

for product in all_products:
    print(product)

    
          

"""