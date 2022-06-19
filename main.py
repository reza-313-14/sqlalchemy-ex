from enum import unique
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# part1
# database+ library://username:password@host:port
engine = create_engine('sqlite:///database.db')
base = declarative_base()

class student(base):
    __tablename__ = 'student'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    
base.metadata.create_all(engine)


# part2
