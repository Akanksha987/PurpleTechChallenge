from sqlalchemy import func

from app.models import Event


def get_store_heatmap(db, store_id):

    rows = (
        db.query(
            Event.zone_id,
            func.count(Event.zone_id),
            func.avg(Event.dwell_ms)
        )
        .filter(
            Event.store_id == store_id,
            Event.zone_id != None
        )
        .group_by(Event.zone_id)
        .all()
    )

    heatmap = {}

    max_visits = max(
        [row[1] for row in rows],
        default=1
    )

    for zone, visits, avg_dwell in rows:

        normalized = int(
            (visits / max_visits) * 100
        )

        heatmap[zone] = {
            "visits": visits,
            "avg_dwell_ms": round(
                avg_dwell or 0,
                2
            ),
            "normalized": normalized
        }

    return heatmap