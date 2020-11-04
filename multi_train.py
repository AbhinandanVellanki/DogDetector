from imageai.Detection.Custom import DetectionModelTrainer


class Trainer():
    def __init__(self):
        self.trainer = DetectionModelTrainer()
        self.trainer.setModelTypeAsYOLOv3()
        # Set name of dataset directory
        self.trainer.setDataDirectory(data_directory="wheels_dataset")
        self.trainer.setTrainConfig(object_names_array=['wheelchair', 'pull trolley', 'push trolley'], batch_size=8, num_experiments=10, train_from_pretrained_model='wheels-yolov3.h5')

    def train(self):
        self.trainer.trainModel()


if __name__ == '__main__':
    trainer_obj = Trainer()
    trainer_obj.train()
