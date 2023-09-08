#Plotting an Image

!pip install opencv-python

import cv2
import matplotlib.pyplot as plt
from skimage import io

lena = io.imread("/content/lena.tif")
plt.imshow(lena);

#plt.xticks([]),plt.yticks([]);   #Used to remove markings of x and y axes