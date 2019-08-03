
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')

wb0 = excel.Workbooks.Open(r'C:\python\so\source.xlsx')
excel.Visible = True

# Move Chart 1 to a new Workbook, which becomes the ActiveWorkbook.
wb0.Charts('Chart1').Move()
excel.ActiveWorkbook.SaveAs(r'C:\python\so\chart1.xlsx')
excel.Application.ActiveWorkbook.Close()

wb0.Charts(2).Move()  # Index number should also work.
excel.ActiveWorkbook.SaveAs(r'C:\python\so\chart2.xlsx')
excel.Application.ActiveWorkbook.Close()

wb1.SaveAs(r'C:\python\so\charts.xlsx')
wb0.SaveAs(r'C:\python\so\no_charts.xlsx')
wb0.Close()
excel.Application.Quit()

##########################################
# Is there a way to move 2 charts at once?
# VBA Codes use loop, selects each chart, flog false.

wb1 = excel.ActiveWorkbook  # Assignment to workbook works.
wb1.Name  # Print filename, should be 'charts.xlsx'.

n = wb0.Charts.Count  # Prints 2.
for chart in n:
    wb0.Charts(1).Select _ False
# False flag does not work for some reason,
# xlLocation seems possible.

# Assignment works.
ch1 = wb0.Charts(1)
ch2 = wb0.Charts(2)
ch1.Name
ch2.Name

####################################

# This example moves Sheet1 after Sheet3 in the active workbook.

Worksheets("Sheet1").Move _ 
 after:=Worksheets("Sheet3")

# Selecting worksheet
sheet = workbook.Worksheets(1) 
sheet = xlApp.ActiveSheet
workbook.Sheets('Sheet1').Select() 

#  Create a new sheet.
new_sheet = wb2.Sheets(wb2.Sheets.Count)
new_sheet.Name = 'Report_1'

# Copy values in sheet 2 to sheet 1.
 ws.Range("A1:AF100").Copy(ws2.Range("A%s:AF%s" % (row, col)))