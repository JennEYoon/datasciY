# Stack Overflow My Answers

This folder is used to test my answers to Stack Overflow questions.  Most of my answers are on Python.  
My Profile on StackOverflow.com: **user: 4693491**  <a href="https://stackoverflow.com/users/4693491/jennifer-e-yoon?tab=profile">Jennifer E. Yoon</a>

A quarter of the answers are about using Excel with Python.  Pywin32 library gives full access to Excel-VBA objects, but only in a Windows OS or Windows Emulation (on Linux).  There are slight changes to commands, but if you are already familiar with VBA, you can do almost everything in Python that you can do in Excel & VBA.  

I find answering questions on Stack Overflow similar to an addictive game.  I need to answer questions quickly in order to gain additional reputation points. :-)

#### Example pywin32 to manipulate Excel files.  

```python
########## Updated on Stackoverflow 6/21/2019 3am. #############  
#
# Refined .Move() method, save new file using Active Workbook property.
#
# This module opens an Excel workbook, splits each worksheet into
# separate files, and saves each Excel file with a new name.  
# The purpose is to preserve extensive formatting of pivot tables 
# in the original Excel workbook, while using Python to split it into
# individual reports.
#
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
wb0 = excel.Workbooks.Open(r'C:\python\so\original.xlsx')
#  This example uses an original Excel workbook with 3 worksheets.
excel.Visible = True

# Move Sheet1
wb0.Worksheets(1).Move()
# The new worksheet becomes the ActiveWorkbook.  Save it as a new Excel file.
excel.Application.ActiveWorkbook.SaveAs(r'C:\python\so\sheet1.xlsx')

# Move Sheet2
wb0.Worksheets(1).Move()
excel.Application.ActiveWorkbook.SaveAs(r'C:\python\so\sheet2.xlsx')  

# Save the single remaining sheet.
wb0.SaveAs(r'C:\python\so\sheet3.xlsx')
wb0.Close()
excel.Application.Quit()

#############################################################  
```

#### Tasks SO as of 8/5/2019 12:22 PM  

 * Create blog demo of using pywin32.
 * Load original.xls file to working directory.
 * Show relative and absolute addressing in python.
 * Post on my website datasciY.com.
 