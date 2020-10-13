# DogDetector

Importable module designed to detect dogs at a single frame of video or a single image and return a list of bounding boxes for each dog detected.

# Create Virtual Env:
$ conda create -n retinanet python=3.6 anaconda
$ source activate retinanet

# Packages Required:
TensorFlow
Numpy
scipy
opencv
pillow
matplotlib
h5py
keras

$ conda install tensorflow numpy scipy opencv pillow matplotlib h5py keras

Downgrade Packages for successful execution:

$ pip install tensorflow==1.14.0
  
  TO USE GPU: $ pip install tensorflow-gpu==1.14.0

$ pip install keras==2.2.0
$ pip install keras_applications==1.0.4

# Download Trained Model:

https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/resnet50_coco_best_v2.0.1.h5

# Install Image AI Library:

$ pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.1/imageai-2.0.1-py3-none-any.whl

# export and import docker image

docker save -o <path for generated tar file> <image name>

docker load -i <path to image tar file>
