import asyncio
import aiohttp
from creat_db import Filmheros, creating_db
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
    session_1 = creating_db()
    async with aiohttp.ClientSession() as session:
        async for people in get_people(range(1, MAX + 1), PARTITION, session):
            print(people)
            session_1.begin()
            session_1.add(Filmheros(birth_year=people['birth_year'],
                          eye_color=people['eye_color'],
                          films=people['films'],
                          gender=people['gender'],
                          hair_color=people['hair_color'],
                          height=people['height'],
                          homeworld=people['birth_year'],
                          mass=people['mass'],
                          name=people['name'],
                          skin_color=people['skin_color'],
                          species=people['species'],
                          starships=people['starships'],
                          vehicles=people['vehicles'],))
            session_1.commit()

            # print(people)

asyncio.run(main())




