import pandas as pd
from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

df = pd.read_excel("modified.xlsx")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_zlabel("z axis")

for i in range(1, 3):
    ax.scatter(df.loc[:,"X" + str(i) + "E2"], df.loc[:,"Y" + str(i) + "E2"], i, c="black", marker="o", s=0.01)

plt.show()