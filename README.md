# DogDetector:

Importable module designed to detect dogs at a single frame of video or a single image and return a list of bounding boxes for each dog detected.

# Pull Docker Image:
`$chmod +x start.sh`
`$./start.sh`

# Download Trained Models:

Retinanet: https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5

YOLO v3: https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5

# Collect Dog Images from COCO Dataset:
1. Download COCO API repo: https://github.com/cocodataset/cocoapi
2. Inside cocoapi/PythonAPI run `$ python setup.py install` 
3. Download Annotations: http://images.cocodataset.org/annotations/annotations_trainval2014.zip
4. Open get_dog_coco.py and set paths accordingly.
5. Run `$ python get_dog_coco.py` and wait till images directory is fully populated

# Install Image AI Library:

`$ pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl`

# export and import docker image:

docker save -o <path for generated tar file> <image name>

docker load -i <path to image tar file>
  
# Run Trainer:
import Trainer from train.py
trainer_obj=Trainer()
trainer_obj.train()

# Run Detector:
import Detector from detect.py
detector_obj=Detector()
bounding_boxes = detector_obj.detect(img=<image/frame>) 


