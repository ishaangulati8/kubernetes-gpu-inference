Client Machine - 
    POST Request to HeadNode : model name & image files
    
    to send request for inference using xception, one batch of images of size 64 (from a folder consisting of only images) :
    for J in {1}; do (curl http://128.105.145.75/inference/xception $(for I in $(ls | tail -n $((64))); do echo -F $I=@$I; done) &); done
    
    to send multiple batches (say 4) of size 64 :
    for J in {1..4}; do (curl http://128.105.145.75/inference/xception $(for I in $(ls | tail -n $((128))); do echo -F $I=@$I; done) &); sleep 0.3; done
    
    where,
    http://128.105.145.75 is address of the headnode that will perform load balancing by distributing the incoming requests to available GPUs nodes
    /inference/xception - path for xception model (at every GPU endpoint)

HeadNode / NGINX - loadbalancer
    
GPU Nodes - execute inference task with image files
    
    Steps
    Download docker image
    Run docker image
