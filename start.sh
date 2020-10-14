docker stop dog_detector
docker rm dog_detector
#docker image rm dog_detector
docker build -t dog_detector .
docker run --gpus all -d --ipc=host -v $(pwd):/workspace/src/ --name dog_detector --network="host" -it dog_detector
docker exec -it dog_detector bash