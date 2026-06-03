import cv2

video_path = "data/videos/CAM 1.mp4"   # adjust name

video = cv2.VideoCapture(video_path)

print("Opened:", video.isOpened())

fps = video.get(cv2.CAP_PROP_FPS)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)

print("FPS:", fps)
print("Frames:", frames)