from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase,sessionmaker


DB_URL = "postgresql+psycopg://postgres:postgres@localhost:5432/restaurant_db"

class Base(DeclarativeBase):
    pass

engine = create_engine(DB_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

with engine.connect() as connection:
    result = connection.execute(text("SELECT 'Connection successful!' AS message;"))
    for row in result:
        print(row.message)