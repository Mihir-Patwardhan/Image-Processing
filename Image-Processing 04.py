#Edge Detection 

import cv2
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

#lena = io.imread("/content/lena.tif")
mountain=io.imread("/content/mountain.jpg")

kernel=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharp=cv2.filter2D(mountain,-1,kernel)
plt.imshow(sharp);
