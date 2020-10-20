from imageai.Detection.Custom import DetectionModelTrainer

class Trainer():
    def __init__(self):
        self.trainer = DetectionModelTrainer()
        self.trainer.setModelTypeAsYOLOv3()
<<<<<<< HEAD
        self.trainer.setDataDirectory(data_directory="dog_dataset") #Set name of dataset directory
        self.trainer.setTrainConfig(object_names_array=['dog'], batch_size=4, num_experiments=10, train_from_pretrained_model='pretrained-yolov3.h5')

=======
        self.trainer.setDataDirectory(data_directory="dog_dataset") #Set name of dataset directory
        self.trainer.setTrainConfig(object_names_array=['dog'], batch_size=4, num_experiments=10, train_from_pretrained_model='pretrained-yolov3.h5')
        
>>>>>>> e809d0e799aa0f669064d423b93280cc101252ec

    def train(self):
        self.trainer.trainModel()
        
if __name__== '__main__':
    trainer_obj=Trainer()
    trainer_obj.train()

        

