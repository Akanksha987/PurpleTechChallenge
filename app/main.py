from typing import List
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.models import Base
from app.database import engine
from app.schemas import EventSchema
from app.models import Event
from app.database import get_db
from app.ingestion import ingest_events
from app.metrics import get_store_metrics
from app.funnel import get_store_funnel
from app.heatmap import get_store_heatmap
from app.anomalies import get_store_anomalies
from app.session_service import build_sessions
from app.models import Transaction
from app.models import Session as VisitorSession

app = FastAPI()
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Store Intelligence API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

@app.post("/events/ingest")
def ingest(
    events: List[EventSchema],
    db: Session = Depends(get_db)
):
    return ingest_events(db, events)

    
@app.get("/stores/{store_id}/metrics")
def metrics(
    store_id: str,
    db: Session = Depends(get_db)
):
    return get_store_metrics(
        db,
        store_id
    )

@app.get("/debug/events")
def get_events(
    db: Session = Depends(get_db)
):
    events = db.query(Event).all()

    return [
        {
            "event_id": e.event_id,
            "visitor_id": e.visitor_id,
            "event_type": e.event_type,
            "store_id": e.store_id
        }
        for e in events
    ]

@app.get("/stores/{store_id}/funnel")
def funnel(
    store_id: str,
    db: Session = Depends(get_db)
):
    return get_store_funnel(
        db,
        store_id
    )


@app.get("/stores/{store_id}/heatmap")
def heatmap(
    store_id: str,
    db: Session = Depends(get_db)
):
    return get_store_heatmap(
        db,
        store_id
    )


@app.get("/stores/{store_id}/anomalies")
def anomalies(
    store_id: str,
    db: Session = Depends(get_db)
):
    return get_store_anomalies(
        db,
        store_id
    )

@app.post("/sessions/build")
def create_sessions(
    db: Session = Depends(get_db)
):
    count = build_sessions(db)

    return {
        "sessions_created": count
    }

@app.get("/debug/transactions")
def debug_transactions(
    db: Session = Depends(get_db)
):
    return {
        "total_transactions":
            db.query(Transaction).count()
    }

@app.get("/debug/sessions")
def debug_sessions(
    db: Session = Depends(get_db)
):
    return {
        "total_sessions":
            db.query(
                VisitorSession
            ).count()
    }