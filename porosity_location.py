import matplotlib.pyplot as plt
from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import time
import datetime
import math

# Loops through the scans to get the location data of the desired pixels using PIL
# Combines the dataframes of each scan to one dataframe and saves them as an Excel file using Openpyxl

root = tk.Tk()
root.withdraw()

print("Select a surface folder:")
path = filedialog.askdirectory() + "/"
print("Processing...")
counter = 1
dataframe_list = []

for scan in os.listdir(path):
    if scan.endswith(".jpg"):

        image = Image.open(path + scan)
        img_width, img_height = image.size
        img_pixel = image.load()

        graph_list_red = []
        graph_list_black = []

        start = time.perf_counter()

        for j in range (0, img_height):
            for i in range(0, img_width):
                if img_pixel[i, j] == (254, 0, 0):
                    graph_list_red.append([i, j])
                if img_pixel[i, j] == (0, 0, 0):
                    graph_list_black.append([i, j])

        end = time.perf_counter()
        time_passed = round((end - start), 2)

        df = pd.DataFrame(graph_list_black)
        df.columns = ["X" + str(counter) + "E" + path.split("/")[7].split(" ")[1], "Y" + str(counter) + "E" + path.split("/")[7].split(" ")[1]]
        
        dataframe_list.append(df)
        
        scan_count = len([scan for scan in os.listdir(path)])
        if counter  == 1:
            print("Time Remaining: " + str(str((datetime.timedelta(seconds=time_passed*scan_count))).split(":")[1]) + " Minutes")

        print(str(counter) + " / " + str(scan_count))
        counter = counter + 1

        # Delete this for all the scans
        if counter == (math.floor((scan_count/2) + 1)):
            df_all_1 = pd.concat([i for i in dataframe_list], sort=False, axis=1)
            to_excel = df_all_1.to_excel("pixel_location_data/" + "sample_" + scan.split(" ")[0] + "/" + "pixel_location_ebene3_" + scan.split(" ")[0] + "_" + scan.split(" ")[1] + "_" +  str(math.floor(scan_count/2)) +  ".xlsx")
            print("First half completed.")
            dataframe_list = [] 
        elif counter == (scan_count + 1):
            df_all_2 = pd.concat([i for i in dataframe_list], sort=False, axis=1)
            to_excel = df_all_2.to_excel("pixel_location_data/" + "sample_" + scan.split(" ")[0] + "/" + "pixel_location_ebene3_" + scan.split(" ")[0] + "_" + scan.split(" ")[1] + "_" +  str(scan_count) + ".xlsx")  
            print("Second half completed.")

# df_all = pd.concat([i for i in dataframe_list], sort=False, axis=1)
# to_excel = df_all.to_excel("pixel_location_data/" + "sample_" + scan.split(" ")[0] + "/" + "pixel_location_ebene3_" + scan.split(" ")[0] + "_" + scan.split(" ")[1] + ".xlsx")