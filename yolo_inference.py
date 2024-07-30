from ultralytics import YOLO


# Load model
model = YOLO('yolov8x')

results = model.predict('input_videos/08fd33_4.mp4', save=True)