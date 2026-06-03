from sqlalchemy import func
from app.models import Session
from app.models import Transaction
from app.models import Event


def get_store_metrics(db, store_id):
    unique_visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.is_staff == False
        )
        .distinct()
        .count()
    )

    entries = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY"
        )
        .count()
    )

    exits = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "EXIT"
        )
        .count()
    )

    avg_dwell = (
        db.query(
            func.avg(Event.dwell_ms)
        )
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_DWELL"
        )
        .scalar()
    )

    queue_depth = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .count()
    )

    abandonment = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_ABANDON"
        )
        .count()
    )

    billing_entries = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .count()
    )

    abandonment_rate = 0

    if billing_entries > 0:
        abandonment_rate = (
            abandonment / billing_entries
        )
    conversion_rate = calculate_conversion_rate(
        db,
        store_id
    )

    return {
    "store_id": store_id,
    "unique_visitors": unique_visitors,
    "entries": entries,
    "exits": exits,
    "avg_dwell_ms": round(avg_dwell or 0, 2),
    "queue_depth": queue_depth,
    "abandonment_rate": round(abandonment_rate, 2),
    "conversion_rate": conversion_rate
}

def calculate_conversion_rate(
    db,
    store_id
):
    total_sessions = (
        db.query(Session)
        .filter(
            Session.store_id == store_id
        )
        .count()
    )

    unique_orders = (
        db.query(
            func.count(
                func.distinct(
                    Transaction.order_id
                )
            )
        )
        .filter(
            Transaction.store_id == store_id
        )
        .scalar()
    )

    if total_sessions == 0:
        return 0

    return round(
        unique_orders /
        total_sessions,
        2
    )