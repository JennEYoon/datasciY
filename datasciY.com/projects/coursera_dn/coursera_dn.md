## How to download Coursera class as tar (zipped, compressed) files.  
You use Linux commands "tar" and "cat" to compress and uncompress files for downloading from Coursera.org.  

1) Go to a Coursera.org course, open the first notebook, click on Jupyter icon (top-left) to access folder-view, move to 1 directory below root, ex., "week1" for course4.  
  
2) Open a new Jupyter notebook at 1 level below root (or any notebook already in the folder).  
   To open a new notebook, from folder-view, click "New" button (top-right), then select Python 3 from drop-down menu.
  
3) At the top of a Jupyter notebook, add some blank cells.  
  
   * Type into a cell "ls" to see the parent folder file list: 
   ``` !ls ../  ``` 
     Run cell (Control + Enter)  
   If files printed are as expected (you're in 1 level below root), type next cell. 

   * Compress and split into 90 MB sizes for downloading:
   ``` !tar chzvf - ../* | split -b 90M - ../"course4.tgz."  ```
     This will create multiple zipped files at the root (parent) level.  
     (You may substitute "course4" with another file name such as "course1".  Make sure your name matches on all places.)
   
4) Go back to folder-view, move up to root level.  
   You should see the .tgz files you have created.  Select and download each file to your computer.  
    
5) From your computer's Linux terminal, uncompress and concatenate the files back into original folders.      
   ``` cat course4.tgz.* | tar xvzf -  ```  
     Review files and check that all were downloaded correctly.  
    
6) Back on Coursera.org Jupyter notebook, delete tar files:  
   ``` !rm -f ../course4.tgz.* ``` 
   ``` !ls -l ../ ```  
  
#### Background:  
You are limited on zip tools you can use on Coursera class servers because you do not have sudo permission to install any software.  You have to use built-in Linux bash tools.  This includes "tar" to compress and split files into binary, fixed size files and "cat" to uncompress and concatenate the files back into original directory structure.  (I use Windows Subsystem for Linux.  This is a Microsoft product with full file compatibility with Windows OS.  You can download WSL app from Microsoft App Store.)  

#### The main commands are:   
  ``` !tar chzvf - ../* | split -b 90M - ../"course4.tgz." ```  (from Coursera.org notebook, create zip files)
  ``` cat course4.tgz.* | tar xvzf - ```  (from your Linux terminal, recombine)
  ``` !rm -f ../course4.tgz.* ```  (from Coursera.org notebook, remove zip files)  
  
  * Change "course4" to other names for your other classes.  Make sure the name matches in all 3 places. 
  * If 90 MB is too large and your downloads hang, try 50 MB size.  Also depends on your internet connection speed.  
  * If you were only able to download week1 and week2, and for some reason your week3 and week4 got corrupted, you can create zip files for just those weeks. First, make sure to delete all zip files you created before.  Then go 1 level below week3, and repeat the instructions.  Then go 1 level below week 4 and repeat.  

#### Link to Coursera.org   
Forum pinned instructions, July 2019 version, for Course 1:   
  * https://www.coursera.org/learn/neural-networks-deep-learning/discussions/forums/a-1G6KlmEeeYBA47k-OCuA/threads/LTMmAazcEemTxQ73F53h-A  
  * Do NOT follow previous instructions. Coursera has changed how their servers are organized several times, so previous instructions do NOT work!  


  -- Jennifer  