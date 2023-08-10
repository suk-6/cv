import torch
import os
from PIL import Image

def parse_yolo_annotation(txtPath, imageWidth, imageHeight):
    with open(txtPath, 'r') as file:
        lines = file.readlines()
    
    annotations = []
    
    for line in lines:
        classId, xCenter, yCenter, boxWidth, boxHeight = map(float, line.strip().split())
        # YOLO 포맷의 좌표를 원래 이미지의 크기로 변환
        xCenter *= imageWidth
        yCenter *= imageHeight
        boxWidth *= imageWidth
        boxHeight *= imageHeight
        
        # 바운딩 박스 정보를 텐서로 변환
        annotation = torch.tensor([xCenter, yCenter, boxWidth, boxHeight, classId])
        annotations.append(annotation)
    
    return annotations

imageFolder = 'images'  # 이미지 폴더 경로
labelFolder = 'labels'  # 라벨 폴더 경로
outputPath = 'export.pt'  # 저장할 .pt 파일 경로

data = []

for imageName in os.listdir(imageFolder):
    if imageName.endswith('.jpg') or imageName.endswith('.PNG'):  # 이미지 파일일 경우
        imagePath = os.path.join(imageFolder, imageName)
        txtPath = os.path.join(labelFolder, f"{imageName[:-4]}.txt")
        
        if os.path.exists(txtPath):
            image = Image.open(imagePath)
            imageWidth, imageHeight = image.size
            
            annotations = parse_yolo_annotation(txtPath, imageWidth, imageHeight)
            
            data.append({
                'image': image,
                'annotations': annotations
            })

# .pt 파일로 데이터 저장
torch.save(data, outputPath)
