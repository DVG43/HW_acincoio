import asyncio
import aiohttp
from more_itertools import chunked


URL = 'https://swapi.dev/api/people/'

MAX = 100
PARTITION = 10

async def get_person(person_id, session):
    async with session.get(f'{URL}{person_id}') as response:
        return await response.json()


async def get_people(all_ids, partition, session):
    for chunk_ids in chunked(all_ids, partition):
        tasks = [asyncio.create_task(get_person(person_id, session)) for person_id in chunk_ids]
        for task in tasks:
            task_result = await task
            yield task_result


async def main():
    async with aiohttp.ClientSession() as session:
        async for people in get_people(range(1, MAX + 1), PARTITION, session):
            print(people)


asyncio.run(main())




# PG_DSN = 'postgresql://dim43:1624@127.0.0.1:5431/for_flask'
#
# engine = create_engine(PG_DSN)   # äêëþ÷åíèå ê áàçå.
# Session = sessionmaker(bind=engine)   # óñòðàèâàåì ðåêóðñèþ - îòêàò
#
# Base = declarative_base()
#
# Base.metadata.create_all(engine)
#
# class Announsment(Base):
#
#     __tablename__ = 'announsments'
#     id = Column(Integer, primary_key=True)
#     headline = Column(String(100), index=True, nullable=False)
#     description = Column(String(200), nullable=False)
#     created_at = Column(DateTime, server_default=func.now())
#     owner = Column(String(50), nullable=False)
#
# class AnnounView(MethodView):
#
#      def post(self):
#         try:
#             validate = CreateAnnounsment(**request.json).dict()
#         except pydantic.ValidationError as error:
#             raise HttpError(400, error.errors())
#
#         with Session() as session:
#             announ = Announsment(headline=validate['headline'],
#                                  description=validate['description'],
#                                  owner=validate['owner'],
#                                  )
#             session.add(announ)
#             session.commit()
#             return {'id': announ.id}
