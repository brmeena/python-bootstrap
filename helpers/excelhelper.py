import sys
import traceback

sys.path.append("../")
import openpyxl
def createExcelFile(excel_file_path,excel_data):
    wb = openpyxl.Workbook()
    sheet = wb.active
    row_counter=1
    for row_item in excel_data:
        col_counter=1
        for col_item in row_item:
            cell =sheet.cell(row=row_counter,column = col_counter)
            cell.value=col_item
            col_counter=col_counter+1
        row_counter=row_counter+1
    wb.save(excel_file_path)
