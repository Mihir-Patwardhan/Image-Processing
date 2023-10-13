#Adding Watermark or Text on an Image

import cv2
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

lena = io.imread("/content/lena.tif")


img2 = np.zeros((512,512,3),np.uint8)+255
cv2.putText(img2,'Mihir',(400,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(255,0,0),2)
plt.show()
Img1 = cv2.addWeighted(lena,0.8,img2,0.2,0)
#Img2 = cv2.addWeighted(monkey,0.8,img2,0.2,0)
images = [Img1]
for i in range(0,len(images)):
  plt.subplot(1,1,i+1)
  plt.imshow(images[i])
plt.show()