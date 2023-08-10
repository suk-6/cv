import torch
import os
from PIL import Image

def parse_yolo_annotation(txt_path, imageWidth, imageHeight):
    with open(txt_path, 'r') as file:
        lines = file.readlines()
    
    annotations = []
    
    for line in lines:
        class_id, xCenter, yCenter, boxWidth, boxHeight = map(float, line.strip().split())
        # YOLO 포맷의 좌표를 원래 이미지의 크기로 변환
        xCenter *= imageWidth
        yCenter *= imageHeight
        boxWidth *= imageWidth
        boxHeight *= imageHeight
        
        # 바운딩 박스 정보를 텐서로 변환
        annotation = torch.tensor([xCenter, yCenter, boxWidth, boxHeight, class_id])
        annotations.append(annotation)
    
    return annotations

image_folder = 'images'  # 이미지 폴더 경로
label_folder = 'labels'  # 라벨 폴더 경로
output_path = 'export.pt'  # 저장할 .pt 파일 경로

data = []

for image_name in os.listdir(image_folder):
    if image_name.endswith('.jpg'):  # 이미지 파일일 경우
        image_path = os.path.join(image_folder, image_name)
        txt_path = os.path.join(label_folder, image_name.replace('.jpg', '.txt'))
        
        if os.path.exists(txt_path):
            image = Image.open(image_path)
            image_width, image_height = image.size
            
            annotations = parse_yolo_annotation(txt_path, image_width, image_height)
            
            data.append({
                'image': image,
                'annotations': annotations
            })

# .pt 파일로 데이터 저장
torch.save(data, output_path)
