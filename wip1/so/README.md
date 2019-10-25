# Stack Overflow My Answers

This folder is used to test my answers to Stack Overflow questions. 
Most of my answers are on Python. 
My Profile on StackOverflow.com: **user: 4693491**  
<a href="https://stackoverflow.com/users/4693491/jennifer-e-yoon?tab=profile">Jennifer E. Yoon</a>

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
 
#### Tasks Update as of 9/19/2019   

 * Got 40 points from 1 question answer!  Same person seems to have seen my recent answer, and voted me up on 3 older answers.  array.array data types and bit and byte.  1 point newbie questioner.  Should be a duplicate of some other SO question.  
 * Follow up on 1 question - numpy memory cache & buffer, 56 GB question.  
   - Do some tests on my own machine.  Specify out=y_array.  
   - Don't waste too much time doing follow up tech support.  I already answered her original questions.  
 * Answer 1 more for this week.  Try for 500 pts.
 * Got 15 pts for curses/ncurses package answer, 1.5 months AFTER I answered it!  
 * Update 9/24/2019 - Got 50 pts from 56 GB Buffer asker on 2 questions!!! 522 pts now.  
 * Task - Look up reading and writing to file numpy array object, recreate buffer problem.  
 * Task - Also tie in with NASA questioner on saving data objects to file. - 10/24/2019.  
 * Task - NASA questioner may be related to Pandas to df object command. Review - 10/24/2019.    
 
 #### Tasks 9/30/2019  
 
* SO to update with loops -- Excel original question.  
* SO numpy automatically naming arrays after its 3D position index.  
  - Task - Update my Answer with **Numpy structured data array**. - 10/24/2019.  
  - Look at link in the Q. https://stackoverflow.com/questions/1373164/how-do-i-create-a-variable-number-of-variables - done.  
    - Most recommend using a dictionary. 
    - Others use list, or a system operation.
 - Numpy indexing ref: 
   https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html#arrays-indexing  

* 532 pts today. My earliest answer on boxplot was voted up, possibley by original questioner, who has 32 pts now, so can vote up.  

#### Update 10/24/2019 StackOverflow  

 * Removed files from SO folder not directly related to items I will post 
   on my blog or Update/revise on StackOverflow.com. 
 * Printed SO Answers list - flagged 3 or 4 to Update/Revise my Answers.  
 * Got Matplotlib 3D plots to work with 3 subplots in a row.- Oct 13-24, 2019.  
   - Can't use Matplotlib style **subplots** method with 3d graphs!  
     ```ax.subplots(row, col, panel)```   
   - Only object oriented method works.  
     ```ax1 = ax.countour3D(projection='3d')```  
