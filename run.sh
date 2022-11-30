sudo docker run  --gpus 'all,"capabilities=compute,utility"' -p 5000:5000 --rm --name=server server:latest
