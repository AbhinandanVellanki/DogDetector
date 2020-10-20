from imageai.Detection.Custom import DetectionModelTrainer

class Trainer():
    def __init__(self):
        self.trainer = DetectionModelTrainer()
        self.trainer.setModelTypeAsYOLOv3()
        self.trainer.setDataDirectory(data_directory="dog_images") #Set name of dataset directory
        self.trainer.setTrainConfig(object_names_array=['dog'], batch_size=4, num_experiments=200, train_from_pretrained_model='pretrained-yolov3.h5')


    def train(self):
        self.trainer.trainModel()
        

