#
# Add a workbook and save (Excel 2007)
# For older versions of excel, use the .xls file extension
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Add()
wb.SaveAs(r'C:\python\so\add_a_workbook.xlsx')  # Woohoo works.  Add r'path'
excel.Application.Quit()

####### Activate one excel file ##############
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb1 = excel.Workbooks.Open(r'C:\python\so\sheet1.xlsx')
wb2 = excel.Workbooks.Open(r'C:\python\so\sheet2.xlsx')
wb3 = excel.Workbooks.Open(r'C:\python\so\sheet3.xlsx')    
excel.Visible = True

# This will open 3 workbooks with wb1 on top.

excel.Application.ActiveWorkbook.Name
# Prints name of currently active workbook, i.e., the one on top.

wb3.Activate()  # puts workbook3 on top
wb2.Activate()  # puts workbook2 on top

### You may need to install pywin32.
### pip install pywin32



####################################################



# Open an existing workbook
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb = excel.Workbooks.Open(r'C:\python\so\test3s.xlsx')
#excel.Visible = True
ws2 = wb.Worksheets('Sheet2')
ws3 = wb.Worksheets('Sheet3')
#Need to pass "Delete" option box.
ws2.Delete()  
ws3.Delete()
wb.SaveAs(r'C:\python\so\test1s.xlsx')
excel.Application.Quit()

#
# Try .Move() method with/without 2 workbooks.
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb0 = excel.Workbooks.Open(r'C:\python\so\split.xlsx')

# Create 2nd workbook file.
wb1 = excel.Workbooks.Add()    
wb1.SaveAs(r'C:\python\so\report1.xlsx')
excel.Visible = True

ws0 = wb0.Worksheets('Sheet1')
ws1 = wb1.Worksheets('Sheet1')
ws2 = wb1.Worksheets.Add(ws0)
ws3 = wb0.Worksheets('Sheet1').Move()
book7 = wb0.Worksheets('Sheet2').Move()
excel.Application.ActiveWorkbook.SaveAs(r'C:\python\so\sh2.xlsx')
excel.Application.Quit()


#
# Refined .Move() method, save new file using Active Worksheet property.
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb0 = excel.Workbooks.Open(r'C:\python\so\original.xlsx')
excel.Visible = True
wb0.Worksheets('Sheet2').Move()
excel.Application.ActiveWorkbook.SaveAs(r'C:\python\so\sheet2.xlsx')
excel.Application.ActiveWorkbook.Close()

wb0.Worksheets('Sheet3').Move()
excel.Application.ActiveWorkbook.SaveAs(r'C:\python\so\sheet3.xlsx')  
excel.Application.ActiveWorkbook.Close()

wb0.SaveAs(r'C:\python\so\sheet1.xlsx')
wb0.Close()
excel.Application.Quit()


#
# Refined .Move() method, in a loop.
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb0 = excel.Workbooks.Open(r'C:\python\so\original.xlsx')
excel.Visible = True

# loop over, example has 3 sheets total, start at 2nd sheet.
for n in range(2, 4):
    wb0.Worksheets(n).Move()
    excel.ActiveWorkbook.SaveAs(r'C:\python\so\report_%s.xlsx' % n)
    excel.ActiveWorkbook.Close()

# Save first sheet & quit.
wb0.SaveAs(r'C:\python\so\report_1.xlsx')
wb0.Close()
excel.Quit()







(workbook.Sheets.Count)
new_sheet = wb2.Sheets(wb2.Sheets.Count)
new_sheet.Name = 'Report_1'

 ws.Range("A1:AF100").Copy(ws2.Range("A%s:AF%s" % (row, col)))


This example moves Sheet1 after Sheet3 in the active workbook.

Worksheets("Sheet1").Move _ 
 after:=Worksheets("Sheet3")


import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
workbook = excel.Workbooks.Open("D:\Desktop\simple_example.xlsx")
sheet = workbook.Worksheets(1) #workbook.Sheets('Sheet1').Select(); 
sheet = xlApp.ActiveSheet
sheet.Cells(1,1).Value="Hello"
workbook.Save()
workbook.Close()
excel.Quit()
sheet = None
book = None
excel.Quit()
excel = None






#
#  Select worksheet1 and save to a new workbook.
#





# #create a new workbook and save it.
# wb2 = excel.Workbooks.Add()
# wb2.SaveAs('report1.xlsx')
# # At this point both excel workbooks are open.

# # Copy sheet1 from source to target.
# ws2 = wb2.worksheets("Sheet1")
# ws2 = wb.worksheets("Sheet2")

