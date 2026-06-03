from app.models import Event


def get_store_anomalies(db, store_id):

    anomalies = []

    queue_depth = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_QUEUE_JOIN"
        )
        .count()
    )

    if queue_depth > 10:
        anomalies.append(
            {
                "type": "QUEUE_SPIKE",
                "severity": "WARN",
                "suggested_action":
                    "Open additional billing counters"
            }
        )

    zone_visits = (
        db.query(Event)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER"
        )
        .count()
    )

    if zone_visits == 0:
        anomalies.append(
            {
                "type": "DEAD_ZONE",
                "severity": "WARN",
                "suggested_action":
                    "Check store traffic"
            }
        )

    return anomalies