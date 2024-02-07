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

    # Check if the database already exists
    cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}'")
    exists = cursor.fetchone()

    # If the database does not exist, create it
    if not exists:
        cursor.execute(f"CREATE DATABASE {db_name}")

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