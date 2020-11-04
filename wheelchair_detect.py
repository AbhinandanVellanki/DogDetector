from imageai.Detection.Custom import CustomObjectDetection

detector = CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("wheels-yolov3.h5")
detector.setJsonPath("wheelchair_dataset/json/detection_config.json")
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image="wheelchair_dataset/validation/images/wheelchair_00742.jpg", output_image_path="result.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])