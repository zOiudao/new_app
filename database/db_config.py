from sqlalchemy import (
    Integer,
    Text,
    Float,
    String,
    ForeignKey,
    Column,
    DateTime,
    create_engine
)
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from os import system as stm
import pytz

tmz = pytz.timezone('America/Sao_Paulo')
ftime = '%d/%m/%Y %H:%M:%S'

db = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(60), unique=True)
    pwd = Column(String(30))
    data = Column(DateTime, default=lambda: datetime.now(tmz))

    def __init__(self, nome, email, pwd):
        self.name = nome
        self.email = email
        self.pwd = pwd
        
class Worker(Base):
    __tablename__ = 'workers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    enterprise = Column(String(50))
    worker_id = Column(String(15), unique=True)
    data = Column(DateTime, default=lambda: datetime.now(tmz))
    
    def __init__(self, name, enterprise, worker_id):
        self.name = name
        self.enterprise = enterprise
        self.worker_id = worker_id

Base.metadata.create_all(db)
