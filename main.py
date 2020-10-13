import cv2
import numpy as np 
from initialize import cam_1,net

def main():
    print(1)
    ct = 0
    while True:
        print(1)
        try:
            ct += 1
            ret_1 = cam_1.grab()
            if ct % 40 == 0:
                ret_1, img_1 = cam_1.retrieve()
                if not ret_1: break
                bboxes = net.detect_objects(img_1)
                if len(bboxes)>0:
                    print(f'Number of dogs: {len(bboxes)}')
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()
