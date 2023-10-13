#Histogram Matching of an Image

import numpy as np
import matplotlib.pyplot as plt

def display(imgs, n, title=''):
    plt.figure(figsize=(20, 26))
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.imshow(imgs[i], 'gray')
        plt.xticks([]), plt.yticks([])
        plt.title(title[i])

def hist_plot(imgs, n, title=''):
    plt.figure(figsize=(10, 7))
    for i in range(n):
        plt.subplot(1, n, i + 1)
        plt.hist(imgs[i].flatten(), bins=256)
        plt.title(title[i] + " Histogram")

def hist_equalize(image):
    hist, bins = np.histogram(image, bins=256, range=(0, 256))

    cdf = hist.cumsum()
    cdf_normalized = (cdf / cdf[-1]) * 255

    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    equalized_image = equalized_image.reshape(image.shape).astype(np.uint8)

    return equalized_image

def histogram_match(image, reference):
    hist_image, _ = np.histogram(image.flatten(), bins=256, range=(0, 256))
    hist_reference, _ = np.histogram(reference.flatten(), bins=256, range=(0, 256))
    cdf_image = hist_image.cumsum()
    cdf_reference = hist_reference.cumsum()
    cdf_image = (cdf_image / cdf_image[-1]) * 255
    cdf_reference = (cdf_reference / cdf_reference[-1]) * 255
    mapping = np.interp(cdf_image, cdf_reference, np.arange(256))
    matched_image = mapping[image]
    matched_image = matched_image.astype(np.uint8)

    return matched_image

image = plt.imread("/content/mountain.jpg")
reference = plt.imread("/content/NegativeMountain.jpg")
modified_image = histogram_match(image, reference)

display([image, reference, modified_image], 3, ['Original Image', 'Reference Image', 'Matched Image'])
hist_plot([image, reference, modified_image], 3, ['Original', 'Reference', 'Matched'])
