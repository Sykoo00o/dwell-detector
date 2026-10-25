from ultralytics import YOLO

# Load a lightweight YOLO model to test your setup
model = YOLO("yolov8n.pt")
print("YOLO is ready to go!")
