from ultralytics import YOLO

# 모델 로드
model = YOLO("yolov8l.pt")
# PyTorch to TensorRT
model.export(format='engine', device=0, half=True)
