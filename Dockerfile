# syntax=docker/dockerfile:experimental

FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
#FROM  nvidia/cuda:11.8.0-base-ubuntu20.04
#FROM ubuntu/latest
RUN apt-get update 
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get install python3.9 python3-pip -y

COPY server.py server.py
COPY reqs.txt reqs.txt
RUN python3.10 -m pip install -U -r reqs.txt

RUN ls /usr/local/cuda-11.8/lib64/
#CMD LD_LIBRARY_PATH=/usr/local/cuda-11.8/lib64 python3.9 server.py
CMD python3.10 server.py
