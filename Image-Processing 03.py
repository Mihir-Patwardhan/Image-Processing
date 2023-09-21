#Negating an Image

import cv2
import matplotlib.pyplot as plt
from skimage import io

lena = io.imread("/content/lena.tif")
monkey = io.imread("/content/image2.tiff")


def negate(image):
  return abs(255-image)

plt.subplot(121)
negative1=negate(monkey)
plt.imshow(negative1);
plt.subplot(122)
negative2=negate(lena)
plt.imshow(negative2);
