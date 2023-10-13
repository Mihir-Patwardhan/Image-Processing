#Smoothing of an image

import cv2
import matplotlib.pyplot as plt
from skimage import io

lena = io.imread("/content/lena.tif")

img=lena
# Linear Smoothing
mean_blur = cv2.blur(img, (5,5))
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Non-linear smoothing
median_blur = cv2.medianBlur(img, 5)
bilateral_blur = cv2.bilateralFilter(img, 9, 60, 15)

# Set up subplots
plt.figure(figsize=(12, 8))

# Original image
plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title("Original Image")

# Linear Smoothing - Mean Blur
plt.subplot(2, 3, 2)
plt.imshow(mean_blur)
plt.title("Mean Blur")

# Linear Smoothing - Gaussian Blur
plt.subplot(2, 3, 3)
plt.imshow(gaussian_blur)
plt.title("Gaussian Blur")

# Non-linear smoothing - Median Blur
plt.subplot(2, 3, 4)
plt.imshow(median_blur)
plt.title("Median Blur")

# Non-linear smoothing - Bilateral Filter
plt.subplot(2, 3, 5)
plt.imshow(bilateral_blur)
plt.title("Bilateral Filter")

plt.tight_layout()
plt.show()
