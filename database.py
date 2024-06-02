from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()


# Создание таблиц
def create_tables():
    metadata.create_all(engine)
