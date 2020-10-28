from imageai.Detection.Custom import DetectionModelTrainer


class Trainer():
    def __init__(self):
        self.trainer = DetectionModelTrainer()
        self.trainer.setModelTypeAsYOLOv3()
        # Set name of dataset directory
        self.trainer.setDataDirectory(data_directory="wheelchair_dataset")
        self.trainer.setTrainConfig(object_names_array=['wheelchair'], batch_size=128, num_experiments=10, train_from_pretrained_model='pretrained-yolov3.h5')

    def train(self):
        self.trainer.trainModel()


if __name__ == '__main__':
    trainer_obj = Trainer()
    trainer_obj.train()
