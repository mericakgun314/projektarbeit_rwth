import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Uses the folder "pixel_location_data"

# Plots a scatter graph of the porosity for a visual representation using Matplotlib.
# Reads the Excel file, which is created by "porosity_location.py" using Openpyxl, and converts it to a pandas dataframe.
# This dataframe is used to plot a scatter graph.

element_input = input("Which element ? (1_1, 1_3 format): ")

root = tk.Tk()
root.withdraw()

print("Select a sample folder containing porosity location data:")
path = filedialog.askdirectory() + "/"

layer = input("Number of layers to plot: ")

for file in os.listdir(path):
    if element_input in file:
        if "first" in file:
            df_1 = pd.read_excel(path + file)
        elif "second" in file:
            df_2 = pd.read_excel(path + file)    

df_all = pd.concat([df_1, df_2], axis=1)

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

for i in range(1, int(layer) + 1):
    ax.scatter(df_all.loc[:,"X" + str(i) + "E3"], df_all.loc[:,"Y" + str(i) + "E3"], i, c="black", marker="o", s=0.001)

plt.show()
