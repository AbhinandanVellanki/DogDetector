import cv2
from detect import Detector
from utils import load_config

def initialize_cameras():
    cam_1 = cv2.VideoCapture(f"rtsp://{CAM_USERNAME_1}:{CAM_PASSWORD_1}@{CAM_IP_1}:554/cam/realmonitor?channel=1@subtype=1")
    return cam_1

config = load_config('configuration.yml')
CAM_IP_1       = config['CAMERA']['IP']['_1']
CAM_USERNAME_1 = config['CAMERA']['USERNAME']['_1']
CAM_PASSWORD_1 = config['CAMERA']['PASSWORD']['_1']

cam_1 = initialize_cameras()
net = Detector()