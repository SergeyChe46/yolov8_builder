from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(data="custom_data.yaml", batch=4, imgsz=640, epochs=50, workers=1)
