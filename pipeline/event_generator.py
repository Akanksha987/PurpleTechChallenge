from datetime import datetime

from app.database import SessionLocal
from app.models import Event

db = SessionLocal()

seen_tracks = set()

seen_zone_entries = set()

seen_billing = set()

def create_entry_event(track_id):

    if track_id in seen_tracks:
        return

    seen_tracks.add(track_id)

    event = Event(
        event_id=f"entry_{track_id}_{int(datetime.now().timestamp()*1000)}",
        store_id="ST1008",
        camera_id="CAM1",
        visitor_id=str(track_id),
        event_type="ENTRY",
        timestamp=str(datetime.now()),
        zone_id=None,
        dwell_ms=0,
        is_staff=False,
        confidence=0.95
    )

    db.add(event)
    db.commit()

    print(f"ENTRY SAVED -> {track_id}")

def create_zone_event(
    track_id,
    zone_name
):

    key = f"{track_id}_{zone_name}"

    if key in seen_zone_entries:
        return

    seen_zone_entries.add(key)

    event = Event(
        event_id=f"zone_{track_id}_{zone_name}_{int(datetime.now().timestamp()*1000)}",
        store_id="ST1008",
        camera_id="CAM1",
        visitor_id=str(track_id),
        event_type="ZONE_ENTER",
        timestamp=str(datetime.now()),
        zone_id=zone_name,
        dwell_ms=0,
        is_staff=False,
        confidence=0.95
    )

    db.add(event)
    db.commit()

    print(
        f"ZONE ENTER -> Visitor {track_id} -> {zone_name}"
    )
    
def create_dwell_event(
    track_id,
    zone_name,
    dwell_ms
):

    event = Event(
        event_id=f"dwell_{track_id}_{int(datetime.now().timestamp()*1000)}",
        store_id="ST1008",
        camera_id="CAM1",
        visitor_id=str(track_id),
        event_type="ZONE_DWELL",
        timestamp=str(datetime.now()),
        zone_id=zone_name,
        dwell_ms=dwell_ms,
        is_staff=False,
        confidence=0.95
    )

    db.add(event)
    db.commit()

    print(
        f"DWELL -> Visitor {track_id} "
        f"Zone {zone_name} "
        f"{dwell_ms} ms"
    )

def create_billing_event(track_id):

    if track_id in seen_billing:
        return

    seen_billing.add(track_id)

    event = Event(
        event_id=f"billing_{track_id}_{int(datetime.now().timestamp()*1000)}",
        store_id="ST1008",
        camera_id="CAM1",
        visitor_id=str(track_id),
        event_type="BILLING_QUEUE_JOIN",
        timestamp=str(datetime.now()),
        zone_id="BILLING",
        dwell_ms=0,
        is_staff=False,
        confidence=0.95
    )

    db.add(event)
    db.commit()

    print(
        f"BILLING QUEUE -> {track_id}"
    )


def create_exit_event(track_id):

    event = Event(
        event_id=f"exit_{track_id}_{int(datetime.now().timestamp()*1000)}",
        store_id="ST1008",
        camera_id="CAM1",
        visitor_id=str(track_id),
        event_type="EXIT",
        timestamp=str(datetime.now()),
        zone_id=None,
        dwell_ms=0,
        is_staff=False,
        confidence=0.95
    )

    db.add(event)
    db.commit()

    print(
        f"EXIT SAVED -> {track_id}"
    )