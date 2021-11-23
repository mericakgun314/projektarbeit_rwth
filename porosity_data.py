from PIL import Image
import os

# Path of the folder, which contains the CT-Scans of all the samples 
path = "C:/Users/User/Desktop/CT Scans Final/"

# Loops the samples
for sample in os.listdir(path):

    # Loops the 15 elements of each sample
    for element in os.listdir(path + sample):

        # Loops the 3 surfaces of each element
        for surface in os.listdir(path + sample + "/" + element):

            # Ignores the files not containing the relevant scans
            if "Ebene" in surface:
                
                # Loops the scans of each surface
                for scan in os.listdir(path + sample + "/" + element + "/" + surface):
                    
                    # Checks for .jpg file
                    if scan.endswith(".jpg"):
                        image = Image.open(path + sample + "/" + element + "/" + surface + "/" + scan)
                