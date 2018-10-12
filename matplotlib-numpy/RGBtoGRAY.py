import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img = mpimg.imread('image.jpg')
gray = rgb2gray(img)
plt.axis('off')
plt.imshow(gray, cmap = plt.get_cmap('gray'))
plt.savefig("RGBtoGray.png", bbox_inches='tight', transparent=True, pad_inches=0, dpi=720)
plt.show()
