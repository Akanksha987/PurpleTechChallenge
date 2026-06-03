from app.models import Event


def get_store_funnel(db, store_id):

    entry = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY",
            Event.is_staff == False
        )
        .distinct()
        .count()
    )

    zone_visit = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER",
            Event.is_staff == False
        )
        .distinct()
        .count()
    )

    billing = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN",
            Event.is_staff == False
        )
        .distinct()
        .count()
    )

    purchase = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "PURCHASE",
            Event.is_staff == False
        )
        .distinct()
        .count()
    )

    return {
        "entry": entry,
        "zone_visit": zone_visit,
        "billing": billing,
        "purchase": purchase
    }