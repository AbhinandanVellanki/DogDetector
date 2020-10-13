import yaml
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2
lineType = 1
color = (255, 255, 255)

def load_config(path_to_config):
    try:
        with open(path_to_config, 'r') as f:
            config = yaml.load(f, Loader=yaml.loader.FullLoader)
    except FileNotFoundError:
        config = None
    return config

def draw_bboxes(img,bboxes):
    for b in bboxes:
        cv2.rectangle(img, (int(b[0]), int(b[1])), (int(b[2]), int(b[3])), (255,255,255), 1)
        if b[5] == 1:
            cv2.putText(img, f"Person", (int(b[2]), int(b[3])), font, fontScale, color, lineType)
        else:
            cv2.putText(img, f"Bicycle", (int(b[2]), int(b[3])), font, fontScale, color, lineType)
    return img