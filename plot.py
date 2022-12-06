
import matplotlib.pyplot as plt
import numpy as np
  

x = ["resnet50", "vgg19", "xception"] # 512
#vgg_x = [1, 2, 16, 32, 64, 128, 256, 320]
#xcep_x = [1, 2, 16, 32, 64, 128, 256, 400]


#res_y = []
# warm start
res_y = [1/44, 2/76, 4/148]
vgg_y = [1/40, 2/60, 4/114]
xcep_y = [1/36, 2/55, 4/88]

y = [900, 320, 400]

fig = plt.figure(figsize = (10, 5))

# creating the bar plot
plt.bar(x, y, color ='green',
		width = 0.4)

plt.xlabel("models")
plt.ylabel("max load")
#plt.title("Students enrolled in different courses")
#plt.show()



#plt.plot(x, y, label = "resnet50 (GPU)")
# plt.plot(x, vgg_y[0], label = "vgg19 (GPU)")
# plt.plot(x, xcep_y[0], label = "xception (GPU)")
# plt.plot(cpu_r_x, cpu_r_y, label = "resnet50 (CPU)", linestyle="dashed")
# plt.plot(cpu_v_x, cpu_v_y, label = "vgg19 (CPU)", linestyle="dashed")
# plt.plot(cpu_c_x, cpu_c_y, label = "xception (CPU)", linestyle="dashed")
plt.legend()
plt.show()


'''
roundtrip
res_x = [1, 2, 16, 32, 64, 128, 256, 512]
vgg_x = [1, 2, 16, 32, 64, 128, 256, 320]
xcep_x = [1, 2, 16, 32, 64, 128, 256, 400]


#res_y = []
# warm start
res_y = [3, 1, 2, 3, 6, 11, 25, 44]
vgg_y = [0.073, 1, 2, 4, 7, 16, 31, 40 ]
xcep_y = [2, 1, 3, 4, 11, 13, 24, 36]

  
# plot lines
plt.plot(res_x, res_y, label = "resnet50 (GPU)")
plt.plot(vgg_x, vgg_y, label = "vgg19 (GPU)")
plt.plot(xcep_x, xcep_y, label = "xception (GPU)")
# plt.plot(cpu_r_x, cpu_r_y, label = "resnet50 (CPU)", linestyle="dashed")
# plt.plot(cpu_v_x, cpu_v_y, label = "vgg19 (CPU)", linestyle="dashed")
# plt.plot(cpu_c_x, cpu_c_y, label = "xception (CPU)", linestyle="dashed")
plt.legend()
plt.show()
'''

'''
cpu vs gpu
res_x = [1, 2, 16, 32, 64, 128, 256, 512]
vgg_x = [1, 2, 16, 32, 64, 128, 256, 320]
xcep_x = [1, 2, 16, 32, 64, 128, 256, 400]
cpu_r_x = [32, 320]
cpu_v_x = [32, 320]
cpu_c_x = [32, 320]

#res_y = []
# warm start
res_y = [0.194, 0.227, 0.402, 0.617, 1.128, 1.566, 2.985, 7.954]
vgg_y = [0.073, 0.090, 0.224, 0.444, 0.836, 1.608, 3.120, 3.926 ]
xcep_y = [0.085, 0.112, 0.269, 0.508, 1.076, 2.025, 3.944, 6.062]

cpu_r_y = [1.3, 11]
cpu_v_y = [2.24, 20.7]
cpu_c_y = [2.2, 17]
  
# plot lines
plt.plot(res_x, res_y, label = "resnet50 (GPU)")
plt.plot(vgg_x, vgg_y, label = "vgg19 (GPU)")
plt.plot(xcep_x, xcep_y, label = "xception (GPU)")
plt.plot(cpu_r_x, cpu_r_y, label = "resnet50 (CPU)", linestyle="dashed")
plt.plot(cpu_v_x, cpu_v_y, label = "vgg19 (CPU)", linestyle="dashed")
plt.plot(cpu_c_x, cpu_c_y, label = "xception (CPU)", linestyle="dashed")
plt.legend()
plt.show()
'''