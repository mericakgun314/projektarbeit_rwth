import numpy
import os
from PIL import Image

path = "C:/Users/User/Desktop/CT Scans Final/1/1 1/Ebene 1/1 1 Ebene 116.jpg"

# image = Image.open(path)
# img_pixel = image.load()

img = numpy.asarray(Image.open(path))

print(img[1].size)