from sqlalchemy.orm import Session

from app.models import Event



def ingest_events(db: Session, events):
    
    print("INGEST CALLED")
    inserted = 0
    duplicates = 0

    for event in events:

        existing_event = (
            db.query(Event)
            .filter(Event.event_id == event.event_id)
            .first()
        )

        if existing_event:
            duplicates += 1
            continue

        db_event = Event(
            event_id=event.event_id,
            store_id=event.store_id,
            camera_id=event.camera_id,
            visitor_id=event.visitor_id,
            event_type=event.event_type,
            timestamp=event.timestamp,
            zone_id=event.zone_id,
            dwell_ms=event.dwell_ms,
            is_staff=event.is_staff,
            confidence=event.confidence,
        )

        db.add(db_event)
        inserted += 1
    db.commit()

    return {
        "inserted": inserted,
        "duplicates": duplicates
    }