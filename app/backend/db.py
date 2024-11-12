from sqlalchemy import create_engine  # позволит запускать БД
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///taskmanager.db', echo=True)  # для связи с базой данных


SessionLocal = sessionmaker(bind=engine)  # создаем сессию связи с БД


class Base(DeclarativeBase):  # DeclarativeBase позволяет объединить наш класс и таблицу с БД
    pass
