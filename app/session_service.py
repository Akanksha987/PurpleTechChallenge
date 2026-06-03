from app.models import Event
from app.models import Session


def build_sessions(db):

    entries = (
        db.query(Event)
        .filter(
            Event.event_type == "ENTRY"
        )
        .all()
    )

    created = 0

    for entry in entries:

        existing = (
            db.query(Session)
            .filter(
                Session.visitor_id ==
                entry.visitor_id
            )
            .first()
        )

        if existing:
            continue

        session = Session(
            visitor_id=entry.visitor_id,
            store_id=entry.store_id,
            entry_time=entry.timestamp,
            exit_time=None,
            converted=False
        )

        db.add(session)

        created += 1

    db.commit()

    return created