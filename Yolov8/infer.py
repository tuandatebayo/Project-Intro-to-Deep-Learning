# Description: This file is used to infer the model on a single image.
from ultralytics import YOLO
import os
import matplotlib.pyplot as plt
import cv2

model = YOLO('yolo_model.pt')
path = 'Data\image-for-infer.jpg'
results = model.predict(path, imgsz=640, conf=0.5)
for r in results:
    cls = r.boxes.cls
    conf = r.boxes.conf
    xyxy = r.boxes.xyxy
def to_label(x):
    labels = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle','bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
    return labels[int(x)]
image = cv2.imread(path)
for i in range(len(cls)):
    label = to_label(cls[i])
    confidence = conf[i]
    [x_min, y_min, x_max, y_max] = [int(k) for k in xyxy[i]]
    width = len(str(label)+' '+str(conf[i])[7:-1]) * 12
    cv2.rectangle(image, (x_min, y_min + 15), (x_min + width, y_min), (255, 0, 255), -1)
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (255, 0, 255), 1)
    cv2.putText(image, str(label)+' '+str(conf[i])[7:-1], (x_min, y_min+15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()