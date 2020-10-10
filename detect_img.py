from imageai.Detection import ObjectDetection

class Detector():
    def __init__(self):
        ## Set up detector
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()

        # Load model
        model_path = 'resnet50_coco_best_v2.0.1.h5'

        detector.setModelPath(model_path)
        detector.loadModel()

        # Set custom object detection for dogs
        # For more options, see: https://github.com/OlafenwaMoses/ImageAI/tree/master/imageai/Detection#---custom-object-detection
        custom_objects = detector.CustomObjects(dog=True)
    
    def detect(self,input_path, output_path):
        # Detect
        detections = self.detector.detectCustomObjectsFromImage(input_image=input_path, output_image_path=output_path, custom_objects=custom_objects, minimum_percentage_probability=45)

if __name__ == '__main__':
    #define unit test case here
    dogdetector=Detector()
    image='test1.jpg'
    result='result.png'
    dogdetector.detect(input_path=image, output_path=result)