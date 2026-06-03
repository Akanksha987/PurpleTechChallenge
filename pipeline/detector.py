from ultralytics import YOLO


class PersonDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):

        results = self.model(
            frame,
            classes=[0],
            verbose=False
        )

        return results