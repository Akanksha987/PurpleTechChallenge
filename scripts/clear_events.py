from app.database import SessionLocal
from app.models import Event

db = SessionLocal()

db.query(Event).delete()

db.commit()

print("Events Cleared")

db.close()