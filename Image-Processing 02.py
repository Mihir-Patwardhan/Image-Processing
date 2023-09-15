#Different Operations on Image

import cv2
import matplotlib.pyplot as plt
from skimage import io
import numpy as np

lena = io.imread("/content/lena.tif")

def scale(image,scale):
    scaleMatrix = np.float32([[scale,0,0],[0,scale,0]])
    dimensions = (image.shape[1],image.shape[0])
    return cv2.warpAffine(image,scaleMatrix,dimensions)

def translate(image,x,y):
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (image.shape[1],image.shape[0])
    return cv2.warpAffine(image,transMatrix,dimensions)

def shear(image,shearVal):
    shearMatrix = np.float32([[1,shearVal,0],[shearVal,1,0]])
    dimensions = (image.shape[1],image.shape[0])
    return cv2.warpAffine(image,shearMatrix,dimensions)

def rotate(image,angle,rotationPoint=None):
    height, width = image.shape[:2]

    if rotationPoint==None:
        rotationPoint = (width//2,height//2)

    rotMatrix = cv2.getRotationMatrix2D(rotationPoint,angle,scale=1.0)
    ''' Alternate Method
    rotMatrix = np.float32([[np.cos(angle),np.sin(angle),0],[-np.sin(angle),np.cos(angle),0]])
    '''

    dimensions = width, height
    return cv2.warpAffine(image,rotMatrix,dimensions)


plt.imshow(scale(lena,2));
plt.imshow(translate(lena,100,150));
plt.imshow(shear(lena,.05));
