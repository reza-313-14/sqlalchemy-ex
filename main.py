from enum import unique
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import relationship

# part1
# database+ library://username:password@host:port
engine = create_engine('sqlite:///database.db') # echo=True
base = declarative_base()
session = sessionmaker(bind=engine)()

class Student(base):
    __tablename__ = 'student'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    classroom_id = Column('classroom_id', Integer, ForeignKey('classroom.id'))


class ClassRoom(base):
    __tablename__ = 'classroom'
    _id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    students = relationship('Student', backref='classroom')
    
base.metadata.create_all(engine)

    
# part2

# select
# students = session.query(Student).order_by(Student.name).all() # .filter(and_(Student._id == 2 , Student.name == 'reza')).order_by(Student.name)
# for student in students:
#     print(student._id, student.name)
# print(students)


# insert
# student_1 = Student(name='mohammad1')
# student_2 = Student(name='mohammad2')

# session.add_all([student_1, student_2])
# session.commit()



# delete
# student = session.query(Student).filter(Student._id == 6).first()
# session.delete(student)
# session.commit()

# student = session.query(Student).filter(Student._id == 5).delete()
# session.commit()


# update
# student = session.query(Student).filter(Student.name == "mohammad").update({'name': 'mohammad ali'})
# session.commit()

# student = session.query(Student).filter(Student.name == 'reza').first()
# student.name = 'reza1'
# session.commit()


# part 3
