import psycopg2
import json
from .dbconfig import conn,cursor
class Order:
    def __init__(self, db_name, user, password):
        self.conn = psycopg2.connect(f"dbname={db_name} user={user} password={password}")
        self.cursor = self.conn.cursor()

    def create_order(self, order_data:dict):
      
        order_dict = json.loads(order_data)

       
        # proper error handling here
        try:
            sql = "INSERT INTO orders (user_id, product_id,quantity) VALUES (%s, %s,%s);"
            values = (order_dict['user_id'], order_dict['product_id'],order_dict['quantity'])
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Order has been inserted successfully.")
        except Exception as e:
            raise ValueError(f"Error inserting order: {e}")
           
    
    def read_order(self, order_id):
       
        try:
            sql = "SELECT * FROM orders WHERE id = %s;"
            self.cursor.execute(sql, (order_id,))
            
            order_data = self.cursor.fetchone()
            print(f"User Data: {order_data}")
        except Exception as e:
            print(f"Error reading user: {e}")
    
    
    def read_all_orders(self) -> list:
          try:
            sql = "SELECT * FROM orders;"
            self.cursor.execute(sql)
            all_orders = self.cursor.fetchall()
            return all_orders
          
          except Exception as e:
            print(f"Error reading all users: {e}")
            return []
 

    
    def delete_order(self, product_id):
        try:
            sql = "DELETE FROM orders WHERE id = %s;"
            self.cursor.execute(sql, (product_id,))
            self.conn.commit()
            return(f"Order with ID {product_id} has been deleted successfully.")
        except Exception as e:
            return(f"Error deleting user: {e}")
   
    
    def close_connection(self):
        self.conn.close()


"""
order_ops = Order(db_name="testdb", user="postgres", password="admin")
order_ops.create_order('{"user_id": "1", "product_id": "2", "quantity":"5"}')
order_ops.read_order(1)



#product_ops.delete_product(3)
all_products = order_ops.read_all_orders()
print("All Products:")

for product in all_products:
    print(product)
order_ops.close_connection()

          

"""