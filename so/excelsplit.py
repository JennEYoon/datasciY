#  Excel sheets split, uses testsplit.xlsx.

from win32com.client import Dispatch

xl = Dispatch('Excel.Application')
wb = xl.Workbooks.Open(r'split.xlsx')

# Save and close the workbook
wb.Close(True)

#
# Add a workbook and save (Excel 2007)
# For older versions of excel, use the .xls file extension
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Add()
wb.SaveAs('add_a_workbook.xlsx')
excel.Application.Quit()