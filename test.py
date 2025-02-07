import torch

# CUDA 사용 가능 여부 확인
print("CUDA 사용 가능:", torch.cuda.is_available())

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
#model.to('cpu')
print("모델 로드 성공")

# 이미지 경로 정의
img = 'https://xn--7o0by2jf8di3kbmew0bjy1b.com/wp-content/gallery/1_natural_family/4.jpg'
print("이미지 경로:", img)

# 추론 수행
results = model(img)
print("추론 완료")

# 결과 출력 및 표시
results.print()
results.show()

# 예측 출력
print("예측 결과:", results.xyxy[0])  # img1 예측 (tensor)
