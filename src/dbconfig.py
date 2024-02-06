import psycopg2
import os
from dotenv import load_dotenv
base_dir = os.path.dirname("D:\\")
file1=os.path.join(base_dir,"test\\.env")
load_dotenv(file1)

db_name= os.getenv('DB_NAME')
user= os.getenv('DB_USER')
password= os.getenv('DB_PASSWORD')
port=os.getenv('DB_PORT')


conn = psycopg2.connect(f"dbname={db_name} user={user} password={password}")
cursor = conn.cursor()
print(db_name)
print(user)
print(password)
print(port)