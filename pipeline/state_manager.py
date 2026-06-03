from datetime import datetime

visitor_states = {}


def update_zone(track_id, zone):

    now = datetime.now()

    if track_id not in visitor_states:

        visitor_states[track_id] = {
            "zone": zone,
            "entry_time": now
        }

        return None

    old_zone = visitor_states[track_id]["zone"]

    if old_zone != zone:

        start_time = visitor_states[track_id]["entry_time"]

        dwell_ms = int(
            (now - start_time).total_seconds() * 1000
        )

        visitor_states[track_id] = {
            "zone": zone,
            "entry_time": now
        }

        return {
            "previous_zone": old_zone,
            "dwell_ms": dwell_ms
        }

    return None