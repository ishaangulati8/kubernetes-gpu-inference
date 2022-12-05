from model_profiler import model_profiler
import tensorflow.keras.applications as apps
import time

'''
dummy model to handle GPU init time
'''

m_resnet =  apps.resnet50.ResNet50(weights='imagenet')
m_vgg19 = apps.vgg19.VGG19(weights='imagenet')
m_xception = apps.xception.Xception(weights='imagenet')

def benchmark(Batch_size):
    profile1 = model_profiler(m_resnet, Batch_size)


    print("----- ResNet50 profile : ")
    print(profile1)

    profile2 = model_profiler(m_vgg19, Batch_size)

    print("----- Vgg19 profile : ")
    print(profile2)

    profile3 = model_profiler(m_xception, Batch_size)

    print("----- Xception profile : ")
    print(profile3)

print("batch size  = 2")
benchmark(2)
time.sleep(2)

print("batch size  = 16")
benchmark(16)
time.sleep(2)

print("batch size  = 32")
benchmark(32)
time.sleep(2)

print("batch size  = 64")
benchmark(64)
time.sleep(2)

print("batch size  = 128")
benchmark(128)
time.sleep(2)

print("batch size  = 256")
benchmark(256)
time.sleep(2)

print("batch size  = 512")
benchmark(512)
time.sleep(2)
