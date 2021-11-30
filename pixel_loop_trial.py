import numpy
import os
from PIL import Image

path = "C:/Users/User/Desktop/CT Scans Final/1/1 1/Ebene 1/1 1 Ebene 116.jpg"

# image = Image.open(path)
# img_pixel = image.load()

img = numpy.asarray(Image.open(path))
img.transpose(2,0,1).reshape(3,-1)
a = 0
b = 0
red_array =numpy.array([254, 0, 0])

for i in img:
    for j in i:
        if (j==red_array).all():
            b= b + 1

print(b)