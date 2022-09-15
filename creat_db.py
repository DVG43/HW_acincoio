
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    Date,
    create_engine,
    func,
)
# from sqlalchemy.dialects.postgresql import UUID





PG_DSN = 'postgresql://пользователь:пароль@127.0.0.1:5431/база данных'

engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(engine)

class Film_heros(Base):

    __tablename__ = 'announsments'
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



class AnnounView(MethodView):

     def post(self):
        try:
            validate = CreateAnnounsment(**request.json).dict()
        except pydantic.ValidationError as error:
            raise HttpError(400, error.errors())

        with Session() as session:
            announ = Announsment(headline=validate['headline'],
                                 description=validate['description'],
                                 owner=validate['owner'],
                                 )
            session.add(announ)
            session.commit()
            return {'id': announ.id}
