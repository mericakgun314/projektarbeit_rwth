import matplotlib.pyplot as plt
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd

root = tk.Tk()
root.withdraw()

print("Select a surface folder:")
path = filedialog.askdirectory() + "/"

counter = 1
dataframe_list = []

for scan in os.listdir(path):
    if scan.endswith(".jpg"):

        image = Image.open(path + scan)
        img_width, img_height = image.size
        img_pixel = image.load()

        graph_list_red = []
        graph_list_black = []

        for j in range (0, img_height):
            for i in range(0, img_width):
                if img_pixel[i, j] == (254, 0, 0):
                    graph_list_red.append([i, j])
                if img_pixel[i, j] == (0, 0, 0):
                    graph_list_black.append([i, j])

        df = pd.DataFrame(graph_list_black)
        df.columns = ["X" + str(counter) + "E" + path.split("/")[7].split(" ")[1], "Y" + str(counter) + "E" + path.split("/")[7].split(" ")[1]]
        
        dataframe_list.append(df)
        
        print(df)
        counter = counter + 1
        
        if counter == 3:
            break

print(dataframe_list)          