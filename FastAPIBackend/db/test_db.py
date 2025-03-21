import asyncio
from db.session import async_session
from sqlalchemy import text

async def test_db_connection():
    async with async_session() as session:
        result = await  session.execute(text("SELECT 1"))
        print(result.scalar())

asyncio.run(test_db_connection())
