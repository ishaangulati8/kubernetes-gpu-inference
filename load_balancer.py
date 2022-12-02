import requests, threading, numpy
from flask import Flask, request

class Worker:
    def __init__(self, ip):
        self.ip = ip
        self.pending_reqs = 0
        self.lock = threading.Lock()

    def __str__(self):
        return 'IP: ' + self.ip + ', pending: ' + str(self.get_pending_reqs())

    def get_pending_reqs(self):
        with self.lock:
            return self.pending_reqs

    def update_pending_reqs(self, n):
        with self.lock:
            self.pending_reqs += n
    
    def forward(self, model, images):
        self.update_pending_reqs(len(images))
        req = requests.post('http://' + self.ip  + ':5000' + '/inference/' + model, files=images)
        self.update_pending_reqs(-len(images))
        return req

workers = ['128.105.144.52', '128.105.144.46', '128.105.144.55']

workers = [Worker(ip) for ip in workers]

app = Flask(__name__)

@app.route('/inference/resnet', methods=['POST'])
def resnet():
    return forward_inference_req('resnet', request.files)
@app.route('/inference/xception', methods=['POST'])
def xception():
    return forward_inference_req('xception', request.files)
@app.route('/inference/vgg19', methods=['POST'])
def vgg19():
    return forward_inference_req('vgg19', request.files)



def forward_inference_req(model, images):
    [print(w) for w in workers]
    worker = workers[numpy.argmin([worker.get_pending_reqs() for worker in workers])]
    req = worker.forward(model, images)
    #print(req)
    return req.content


app.run(host='0.0.0.0', port=5000)
