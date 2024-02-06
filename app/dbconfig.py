import psycopg2
import os
from dotenv import load_dotenv
from sqlmodel import Session, SQLModel, create_engine
from . import model


base_dir = os.path.dirname("D:\\")
file1 = os.path.join(base_dir, "test\\.env")
load_dotenv(file1)

db_name = os.getenv('DB_NAME3')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')
dbhost = os.getenv('DB_HOST')

dburl = f"postgresql://{user}:{password}@{dbhost}:{port}/{db_name}"

engine = create_engine(dburl)


def create_db():
    conn = psycopg2.connect(database="postgres", user=user, password=password, host=dbhost, port=port)
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Use CREATE DATABASE IF NOT EXISTS to avoid errors if the database already exists
    query = f'CREATE DATABASE IF NOT EXISTS {db_name}'
    cursor.execute(query)
    
    conn.close()
    SQLModel.metadata.create_all(engine)


def create_table():
    SQLModel.metadata.create_all(engine)

def init_db():
    try:
        create_table()
    except:
        create_db()


def get_session():
    with Session(engine) as session:
        yield session