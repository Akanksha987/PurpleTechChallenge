import cv2
import supervision as sv

from pipeline.exit_manager import update_exit
from pipeline.state_manager import update_zone
from pipeline.event_generator import (
    create_billing_event,
    create_entry_event,
    create_zone_event,
    create_dwell_event,
    create_exit_event
)
from pipeline.detector import PersonDetector
from pipeline.tracker import VisitorTracker
from pipeline.zones import get_zone

video_path = "data/videos/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Failed to open video")
    exit()

detector = PersonDetector()
tracker = VisitorTracker()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Video Finished")
        break

    results = detector.detect(frame)

    detections = sv.Detections.from_ultralytics(
        results[0]
    )

    tracked = tracker.update(
        detections
    )

    annotated = results[0].plot()

    current_tracks = []

    if tracked.tracker_id is not None:

        current_tracks = [
            int(x)
            for x in tracked.tracker_id
        ]

        for i, track_id in enumerate(
            tracked.tracker_id
        ):

            create_entry_event(
                int(track_id)
            )

            x1, y1, x2, y2 = tracked.xyxy[i]

            center_x = int(
                (x1 + x2) / 2
            )

            center_y = int(
                (y1 + y2) / 2
            )

            print(
                f"Track {track_id} center=({center_x},{center_y})"
            )

            cv2.circle(
                annotated,
                (center_x, center_y),
                6,
                (0, 0, 255),
                -1
            )

            zone = get_zone(
                center_x,
                center_y
            )

            if zone:

                if zone == "BILLING":

                    create_billing_event(
                        int(track_id)
                    )

                print(
                    f"Visitor {track_id} entered {zone}"
                )

                create_zone_event(
                    int(track_id),
                    zone
                )

                result = update_zone(
                    int(track_id),
                    zone
                )

                if result:

                    create_dwell_event(
                        int(track_id),
                        result["previous_zone"],
                        result["dwell_ms"]
                    )

    # ---------------------------
    # EXIT DETECTION
    # ---------------------------

    exited_tracks = update_exit(
        current_tracks
    )

    for track_id in exited_tracks:

        create_exit_event(
            track_id
        )

    # ---------------------------
    # DRAW ZONES
    # ---------------------------

    cv2.rectangle(
        annotated,
        (100, 100),
        (400, 300),
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated,
        "SKINCARE",
        (100, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.rectangle(
        annotated,
        (500, 100),
        (700, 300),
        (255, 0, 0),
        2
    )

    cv2.putText(
        annotated,
        "BILLING",
        (500, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow(
        "Store Intelligence",
        annotated
    )

    key = cv2.waitKey(30)

    if key == 27:
        print("ESC Pressed")
        break

    try:
        if cv2.getWindowProperty(
            "Store Intelligence",
            cv2.WND_PROP_VISIBLE
        ) < 1:
            print("Window Closed")
            break
    except:
        break
    
# Save EXIT for all active visitors

if tracked.tracker_id is not None:

    for track_id in tracked.tracker_id:

        create_exit_event(
            int(track_id)
        )

cap.release()
cv2.destroyAllWindows()
