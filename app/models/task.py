from app.backend.db import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.models import user
from slugify import slugify

#

class Task(Base):  # модель Task, наследованную от ранее написанного Base
    __tablename__ = 'tasks'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=True, index=True)
    # ForeignKey внешний ключ на id из таблицы 'users'
    # ondelete='CASCADE' для удаления tasks при удалении users
    slug = Column(String)
    user = relationship('User', back_populates='tasks')  # объект связи с таблицей User



from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))
