from imageai.Detection import ObjectDetection

class Detector():
    def __init__(self):
        ## Set up detector
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()

        # Load model
        model_path = 'resnet50_coco_best_v2.0.1.h5'
        self.detector.setModelPath(model_path)
        self.detector.loadModel()

        # Set custom object detection for dogs
        # For more options, see: https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection#---custom-object-detection
        self.custom_objects = self.detector.CustomObjects(dog=True)
    
    def detect(self,input_path, output_path):
        # Detect
        detections = self.detector.detectCustomObjectsFromImage(input_image=input_path, output_image_path=output_path, custom_objects=self.custom_objects, minimum_percentage_probability=45)
        bounding_boxes=[]
        for d in detections:
            bounding_boxes.append(d['box_points'])
        return bounding_boxes

if __name__ == '__main__':
    #define unit test case here
    dogdetector=Detector()
    image_frame='test1.jpg'
    result='result.png'
    detected_boxes=dogdetector.detect(input_path=image_frame, output_path=result)
    print(len(detected_boxes),"dogs detected at:", detected_boxes)