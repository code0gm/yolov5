import mss #mss 버전이 최신이 10인데 오류나서 8로 재설치함 pip install mss==8.0.0
import numpy as np
import cv2
import time
import keyboard
import torch #cuda118로 설치함 pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
import win32gui

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def get_active_window_client_rect():
    hwnd = win32gui.GetForegroundWindow()
    client_rect = win32gui.GetClientRect(hwnd)
    left, top = win32gui.ClientToScreen(hwnd, (client_rect[0], client_rect[1]))
    right, bottom = win32gui.ClientToScreen(hwnd, (client_rect[2], client_rect[3]))
    return left, top, right, bottom

size = get_active_window_client_rect()
print(size)
with mss.mss() as sct:
    monitor = {"top": 50, "left": 50, "width": 1600, "height": 1000}
    
while True:
    t = time.time()
    
    img = np.array(sct.grab(monitor))
    
    result = model(img)
    
    # Render the result and squeeze the dimensions
    rendered_result = np.squeeze(result.render())

    # Resize the image to 50% of its original size
    resized_result = cv2.resize(rendered_result, (0, 0), fx=0.5, fy=0.5)

    cv2.imshow("result", resized_result)
    
    print('fps:', 1/(time.time()-t))
    
    cv2.waitKey(1)
    
    if keyboard.is_pressed('q'):
        break
    
cv2.destroyAllWindows()