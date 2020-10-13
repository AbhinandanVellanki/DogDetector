#FROM nvidia/cuda:10.2-runtime-ubuntu18.04

FROM tensorflow/tensorflow:1.14.0-gpu-py3

WORKDIR /workspace/src/

COPY . .

RUN apt-get -y update 

RUN apt-get -y install python3-pip 

RUN apt-get -y install nano

RUN pip3 install -r requirements.txt

RUN apt -y install cmake

RUN apt-get install -y libsm6 libxext6 libxrender-dev

RUN pip3 install opencv-python==4.2.0.34

ENTRYPOINT bash