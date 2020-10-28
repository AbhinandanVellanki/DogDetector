from imageai.Prediction import ImagePrediction
import os
prediction = ImagePrediction()

#choose model
prediction.setModelTypeAsSqueezeNet()
prediction.setModelTypeAsResNet()
prediction.setModelTypeAsInceptionV3()
prediction.setModelTypeAsDenseNet()

#set model path
model_filename = "DenseNet-BC-121-32.h5" # path/filename of model in working directory
prediction.setModelPath(os.path.join(os.getcwd(), model_filename))
prediction.loadModel(prediction_speed="fast") # available : "normal", "fast", "faster", "fastest"

predictions, probabilities = prediction.predictImage(image_input="test1.jpg", input_type='file', result_count=10)
for prediction, probability in zip(predictions, probabilities):
    print(prediction, probability)
     