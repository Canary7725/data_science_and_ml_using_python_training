# YOLO


# You Only Look Once
# Real Time Object Detection in a single forward pass

# YOLO is a deep learning-based object detection algorithm that can detect mutliple objects in an image extremely fast. Unlike older methods, they can scan multiple images at the same time. YOLO works by:

# 1. Bounding Box
# 2. Object Class
# 3. Confidence Score


from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Detect objects in image
results = model("image.jpg")

# Display image with detected boxes
results[0].show()
