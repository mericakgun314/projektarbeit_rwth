from openpyxl.workbook import Workbook
from openpyxl import load_workbook

wb = load_workbook("porosity_data_sample_1.xlsx")
ws = wb.active

print(ws["D2"].value)