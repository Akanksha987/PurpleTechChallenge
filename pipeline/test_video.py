import cv2

video_path = "data/videos/CAM 1.mp4"

cap = cv2.VideoCapture(video_path)

print("Opened:", cap.isOpened())

print(
    "Frames:",
    cap.get(cv2.CAP_PROP_FRAME_COUNT)
)

print(
    "FPS:",
    cap.get(cv2.CAP_PROP_FPS)
)

cap.release()