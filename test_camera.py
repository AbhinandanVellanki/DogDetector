import cv2
CAM_IP_1 = '192.168.50.108'
CAM_PASSWORD_1 = 'admin888888'
CAM_USERNAME_1 = 'admin'
cam_1 = cv2.VideoCapture(f"rtsp://{CAM_USERNAME_1}:{CAM_PASSWORD_1}@{CAM_IP_1}:554/cam/realmonitor?channel=1@subtype=1")
ret_1= cam_1.grab()
ret_1, img_1 = cam_1.retrieve()
print(ret_1)
