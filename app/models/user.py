from app.backend.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from slugify import slugify



class User(Base):  # модель User, наследованную от ранее написанного Base
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String)
    tasks = relationship('Task', back_populates='user', cascade='save-update, merge, delete, delete-orphan')  # объект связи с таблицей Task


print(CreateTable(User.__table__))