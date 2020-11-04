from imageai.Detection import ObjectDetection
import time
import os
import cv2
import numpy as np

class Detector():
    def __init__(self):
        ## Set up detector
        self.detector = ObjectDetection()

        # Load model
        self.detector.setModelTypeAsYOLOv3()
        #self.detector.setModelTypeAsRetinaNet()
        model_name= 'yolov3-dogs.h5' #SET TO NAME OF DESIRED MODEL OF USE
        model_path=os.path.join(os.getcwd(), model_name)
        self.detector.setModelPath(os.path.join(os.getcwd(),model_path))
        self.detector.loadModel()

        # Set custom object detection for dogs
        # For more options, see: https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection#---custom-object-detection
        self.custom_objects = self.detector.CustomObjects(dog=True)
    
    def detect(self,img):
        # Detect
        _ , detections = self.detector.detectCustomObjectsFromImage(input_type = "array",
                                                                    input_image= img,
                                                                    output_type = "array",
                                                                    custom_objects=self.custom_objects,
                                                                    minimum_percentage_probability=80)
        bounding_boxes=[]
        for d in detections:
            bounding_boxes.append(d['box_points'])
        return bounding_boxes

if __name__ == '__main__':
    #define unit test case here
    t1=time.time()
    dogdetector=Detector()
    print("Initialization Time: ", time.time()-t1)
    #image_frame='test1.jpg'
    image_frame = np.array(cv2.imread('test2.jpg'))
    print(np.shape(image_frame))
    result='result.png'
    t1=time.time()
    detected_boxes=dogdetector.detect(img=image_frame)
    print("Inference Time: ", time.time()-t1)
    print(len(detected_boxes),"dogs detected at:", detected_boxes)
