from openpyxl.workbook import Workbook
from openpyxl import load_workbook
import os

for file in os.listdir("C:/Users/User/Documents/github_repos/projektarbeit_rwth/"):
    if file.endswith(".xlsx"):
        wb = load_workbook(file)
        ws = wb.active

        ws.unmerge_cells("A1:A3")
        ws.delete_cols(1, 2)

        file_split = file.split("_")

        scan_count = len([scan for scan in os.listdir("C:/Users/User/Desktop/CT Scans Final/" + file_split[3] + "/" + file_split[3] + " " + file_split[4].split(".")[0] + "/" + "Ebene 1")])

        ws.insert_rows(1)
        ws.insert_cols(1)

        ws["A2"].value = "Ebene 1"
        ws["A3"].value = "Ebene 2"
        ws["A4"].value = "Ebene 3"

        a = 0

        for cell in ws[1]:
            cell.value = a
            a = a + 1
            if a == scan_count + 1:
                break

        ws["A1"].value = None

        wb.save("df_" + file_split[3] + "/df_" + file_split[3] + "_" + file_split[4])