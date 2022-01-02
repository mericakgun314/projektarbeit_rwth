from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from PIL import Image
import os

# BACKUP, NOT THE MAIN FILE

directory = r"C:/Users/Meriç/Desktop/Ebene 3"

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

a = 1
Z = [a]
graph_list_red = []
colored_pixel_count = 0
red_pixel_count = 0

for filename in os.listdir(directory):
    xb = []
    yb = []
    xr = []
    yr = []

    if filename.endswith(".jpeg"):
        image = Image.open(os.path.join(directory, filename))
        img_width, img_height = image.size # Width and Hight of the image
        indv_pix = image.load()
        
        graph_list_black = []

        print(filename)
        
        for j in range (0, img_height):
            for i in range(0, img_width):
                if indv_pix[i, j] != (0, 0, 0):
                    colored_pixel_count = colored_pixel_count + 1
                if indv_pix[i, j] == (254, 0, 0):
                    red_pixel_count = red_pixel_count + 1 
                    graph_list_red.append([i, j])  
                if indv_pix[i, j] == (0, 0, 0):
                    graph_list_black.append([i, j])

        # print((((colored_pixel_count - red_pixel_count) / ((img_height * img_width) - red_pixel_count))) * 100)
        for i in graph_list_red:
            xr.append(i[0])
            yr.append(i[1])
        for i in graph_list_black:
            xb.append(i[0])
            yb.append(i[1])

        ax.scatter(xb, yb, Z, c="black", marker="o", s=0.01)

        ax.scatter(xr, yr, Z, c="r", marker="o", s=0.01)

        a = a + 1
        Z.clear()
        Z.append(a)
        
plt.show()            