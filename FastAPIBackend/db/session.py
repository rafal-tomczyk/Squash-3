from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from config import get_settings

# Tworzymy instancję settings dopiero gdy jest potrzebna
settings = get_settings()
DATABASE_URL = settings.DB_CONNECTION_LINK

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
