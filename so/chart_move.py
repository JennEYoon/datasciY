
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')

wb0 = excel.Workbooks.Open(r'C:\python\so\source.xlsx')
excel.Visible = True

# Move Chart 1 to a new Workbook, which becomes the ActiveWorkbook.
wb0.Charts('Chart1').Move()
excel.ActiveWorkbook.SaveAs(r'C:\python\so\charts.xlsx')
wb1 = excel.ActiveWorkbook
wb1.Name  # Print filename, should be 'charts.xlsx'.

# Move 2 charts to a new workbook.
n = wb0.Charts.Count  # Prints 2.
ch1 = wb0.Charts(1)
ch2 = wb0.Charts(2)

for chart in n:
    wb0.Charts(1).Select



excel.Application.ActiveWorkbook.Close()

wb1.SaveAs(r'C:\python\so\charts.xlsx')
wb0.SaveAs(r'C:\python\so\no_charts.xlsx')
wb0.Close()
excel.Application.Quit()