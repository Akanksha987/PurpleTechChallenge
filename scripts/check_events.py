from asyncio import events

from app.database import SessionLocal, engine
from app.models import Event
from app.models import Base
db = SessionLocal()


Base.metadata.create_all(bind=engine)

print(db.query(Event).count())

print("Database Created")
db.close()