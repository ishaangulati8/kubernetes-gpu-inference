from flask import Flask, request
import requests
#import shutil
#from tensorflow.keras.applications.resnet50 import ResNet50
#from tensorflow.keras.preprocessing import image
import tensorflow.keras.applications as apps
#from tensorflow.keras.applications.resnet50 # import preprocess_input, decode_predictions
import numpy as np
import cv2
import os
import time
#from cupyx.profiler import benchmark
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
from urllib.request import urlopen
app = Flask(__name__)

TOP_X_PRED = 3

models = {'resnet': apps.resnet50.ResNet50(weights='imagenet'), \
    'xception': apps.xception.Xception(weights='imagenet'), \
    'vgg19': apps.vgg19.VGG19(weights='imagenet')}

preprocess_function = {'resnet': apps.resnet50.preprocess_input, 'xception': apps.xception.preprocess_input, \
    'vgg19':apps.vgg19.preprocess_input}

decode_function = {'resnet': apps.resnet50.decode_predictions, 'xception': apps.xception.decode_predictions, \
    'vgg19':apps.vgg19.decode_predictions}

image_shape = {'resnet': (224,224), 'xception': (299,299), 'vgg19': (224,224)}
@app.route('/inference/resnet', methods=['POST'])
def resnet():
    return process_inference_req('resnet', request.files)
@app.route('/inference/xception', methods=['POST'])
def xception():
    return process_inference_req('xception', request.files)
@app.route('/inference/vgg19', methods=['POST'])
def vgg19():
    return process_inference_req('vgg19', request.files)


def process_inference_req(model, image_files):
    #print(model, image_files)
    start = time.process_time()
    images = []
    names = []
    for name in image_files.keys():
        #print(name)
        names.append(name)
        image = cv2.imdecode(\
                    np.frombuffer(\
                        image_files[name].read(),\
                    np.uint8),\
                cv2.IMREAD_COLOR)
        #print(image)
        images.append(cv2.resize(image, image_shape[model]))
        '''
        images.append(\
            cv2.resize(\
                cv2.imdecode(\
                    np.frombuffer(\
                        image_files[name].read(),\
                    np.uint8),\
                cv2.IMREAD_COLOR),\
            image_shape[model])
        )
        '''
    images = preprocess_function[model](np.array(images))
    predictions = decode_function[model](models[model].predict_on_batch(images), top=TOP_X_PRED)
    end = time.process_time() - start
    print("--time = "+ str(end) )
    return format_output(predictions, names, end)

def format_output(preds, names, t):
    out = ""
    for i in range(len(preds)):
        out += "Top " + str(TOP_X_PRED) + " Predictions for " + names[i] + ":\n"
        for j in range(TOP_X_PRED):
            out += "\t" + str(j) + " - " + preds[i][j][1] + ", confidence = " + str(preds[i][j][2])
            out += "\n"
        out += "\n"
    out += "time taken = " + str(t) + "s"
    return out
    '''
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        body = request.json
        model_name = body["model"]
        img_url = body["url"]
        #print(model_name)
        #print(img_url)
        #shape = (299,299) if model_name == 'xception(224,224)
        imgfile = download_img(img_url, image_shape[model_name])
        if imgfile is not None:
            output = run_model(model_name, imgfile)
            return output
            #return Response(json.dumps(output),  mimetype='application/json')
    else:
        return "error"
    '''
def run_model(model, img_path):
    #model = ResNet50(weights='imagenet')
    #img_path = 'elephant.jpg'
    #img = image.load_img(img_path, target_size=(224, 224))
    #x = image.img_to_array(img)
    x = img_path
    x = np.expand_dims(x, axis=0)
    x = preprocess_function[model](x)

    preds = models[model].predict_on_batch(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    # Predicted: [(u'n02504013', u'Indian_elephant', 0.82658225), (u'n01871265', u'tusker', 0.1122357), (u'n02504458', u'African_elephant', 0.061040461)]
    return decode_function[model](preds, top=3)[0][0][1]

def download_img(url, shape):
    image = urlopen(url).read()
    image = cv2.imdecode(np.frombuffer(image, np.uint8), cv2.IMREAD_COLOR)
    return cv2.resize(image,shape)
def download_img_old(url):
    file_name = "test_img.jpg"
    res = requests.get(url, stream = True)
    if res.status_code == 200:
        with open(file_name,'wb') as f:
            shutil.copyfileobj(res.raw, f)
        print('Image sucessfully Downloaded: ',file_name)
        return file_name
    else:
        print('Image Couldn\'t be retrieved')
        return None

if __name__ == "__main__":
    #app.run()
    app.run(host='0.0.0.0', port=5000)
