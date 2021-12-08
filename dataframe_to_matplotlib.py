import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Plots a scatter graph of the porosity for a visual representation using Matplotlib.
# Reads the Excel file, which is created by "porosity_location.py" using Openpyxl, and converts it to a pandas dataframe.
# This dataframe is used to plot a scatter graph.

element_input = input("Which element ? (1_1, 1_3 format): ")

df = pd.read_excel("pixel_location_data/sample_1/pixel_location_ebene3_" + str(element_input) + ".xlsx") # Change accordingly

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

for i in range(1, 3):
    ax.scatter(df.loc[:,"X" + str(i) + "E3"], df.loc[:,"Y" + str(i) + "E3"], i, c="black", marker="o", s=0.01)

plt.show()