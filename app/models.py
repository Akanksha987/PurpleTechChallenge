from sqlalchemy import Column, String, Integer, Boolean, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Event(Base):
    __tablename__ = "events"

    event_id = Column(String, primary_key=True)

    store_id = Column(String)
    camera_id = Column(String)

    visitor_id = Column(String)

    event_type = Column(String)

    timestamp = Column(String)

    zone_id = Column(String)

    dwell_ms = Column(Integer)

    is_staff = Column(Boolean)

    confidence = Column(Float, nullable=True, default=0.0)

class Session(Base):
    __tablename__ = "sessions"

    visitor_id = Column(String, primary_key=True)

    store_id = Column(String)

    entry_time = Column(String)

    exit_time = Column(String)

    converted = Column(Boolean, default=False)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    order_id = Column(String)

    store_id = Column(String)

    order_date = Column(String)

    order_time = Column(String)

    total_amount = Column(Float)