import sys
import traceback

sys.path.append("../")
from helpers import excelhelper
try:
    data=[["t1","t2"]]
    excelhelper.createExcelFile("test.xlsx",data)
except Exception as e:
    traceback.print_exc(e)
