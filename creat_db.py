
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Date,
    create_engine,
    )
# from sqlalchemy.dialects.postgresql import UUID

PG_DSN = 'postgresql://пользователь:пароль@127.0.0.1:5431/база данных'

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)


class Filmheros(Base):

    __tablename__ = 'film_heros'
    id = Column(Integer, primary_key=True)
    birth_year = Column(Date())
    eye_color = Column(Text())
    films = Column(String(2000)) # строка с названиями фильмов через запятую
    gender = Column(Text())
    hair_color = Column(Text())
    height = Column(String(10))
    homeworld = Column(String(100))
    mass = Column(String(10))
    name = Column(String(100), nullable=False)
    skin_color = Column(String(100))
    species = Column(String(2000)) # строка с названиями типов через запятую
    starships = Column(String(2000)) # строка с названиями кораблей через запятую
    vehicles = Column(String(2000)) # строка с названиями транспорта через запятую


def creating_db():
    session_db = Session()
    Base.metadata.create_all(engine)
    return session_db