# Idea - from Data Science teacher 
Easiest way for new ML users to set up and run small CNN models.  

#### CoLab notebook  
environment.yml file  
Download data  
Save loaded libraries.
Save to Google Drive (user account)  
What cells instructor can setup, with 1 page instruction, for students to get started using ML.  
$200 credit, can use to try out higher core GPUs.  
Lower core GPUs free now!  

Instuctions for installing packages and saving these settings to Google Drive. 
Instructions for using CoLab with environment.yml file and "conda activate name" in shell.  

from jupyter cell> 
!pwd
!conda activate name -- doesn't work.  Can choose engine.  Save env as an engine.  

#### Binder -- 100 user hard max.  
Conference like SciPy is too many people, and many trying repeatedly to launch binder, so each 
person may start multiple instances, compounding the problem.  
Builds environment from "environment.yml" file, so pkg management is handled.  
Data is small enough to reside at same place on Github, with notebooks.  
Data can link to URL if large, download but saved for next time notebook is run. 


