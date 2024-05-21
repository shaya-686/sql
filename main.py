from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

with open("config.json", "r") as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/schooldb'
engine = create_engine(db_url)

Base = declarative_base()


# create table users

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_sec'), primary_key=True)
    name = Column(String(20))
    age = Column(Integer)


# add table to db
Base.metadata.create_all(bind=engine)

