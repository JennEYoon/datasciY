# Notes on Areteus project, public here  
Private notes in Jennifer-Yoon private repo.  

### Dec 22, 2024 Sunday notes:  

 * Find Colab pricing, $10/month pro?  Better GPU?
   - Pay as you Go: $10/month for 100 compute units, expire in 90 days unused units. ** start here, if needed **  
   - Colab Pro: $10/month for 100 compute units, expire after 90 days unused units, get more memory machines (not needed for data sizes), get terminal (VM machine).  
 * Find AI pricing, which ones are good for me? 
   
Try running DataLoader from ECGTransform paper during Christmas post week break.  
Write-up do, present to Bill, Dec 2024 end - January 7, 2025.  
Present to Dan & Peter from small group in January 2025.  
 * Show some to Jason, Rodrigo - Jan 7, 2025 call, Tuesday.

### Make timesheet, present contract employee/shareholder  
From October calls, Nov, Dec.  
Total about 3 weeks worth so far (80-120 hours), including this week.  
Employment contact, stipulate I can publish my own work on events/publications/my website, but keep all data produced by Areteus private.  If Areteus decideds to make a portion of data public, I can use that data, but eh decision will be up to Jason and other at Areteus.  

> * Goal Jason: To have a working prototype with AI prediction (may not be live) by May-June 2025, 6 months.
> Fallback: Use not-live data.  Use Hospital ECG from Mexico data, to show AI part works.  Show device data separately that may not be clean.
> Fallback: Use someone else's device with 2 or more leads, or buy 2 devices used together with 1-lead each, get data, showcase AI part works.
> Fallback: Use live data from only 2 of Jason's 12-19 lead, use "live" to showcase proof of concept, device and AI works.

### Database, my thoughts:  
DART - language, CloudFlare, fine.  

Use no-SQL structure to import and store data, unmodified/written.  
Use SQL - to save portions, each customer's data file separately saved, saved time later on export.  
Use temp file to gather data from each cloud upload sessions, one per user, then when data is finished uploading and checked, save one permanent copy for later audits, then add chuck to no-SQL dabase.  Add date-time-timezone, location, user ID, logs about upload, errors etc.  

Each chunk to data upload will be one-day's worth of data for each user, written into consequtive rows into no-SQL table.  
Each User ID has a SQL-Table datavase for all historical data.  Live data is not uploaded until sync time.  
User web interface allows searching by date and time, view heart-rate graphs, and see AI diagnostic analysis on any day-hour period.  
Live USB-phone user-interface, provide alerts for irregular heart-beat, based on simple AI prediction model, continuously run on client phone.  
Overnight, run detailed AI anlalysis on uploaded heart-rate analysis.  Trends spotted to go for hospital checkups, precautions.  

### Dec 24, 2024 thoughts:  

Working on reading train.py and test.py (PyTorch format files used by ECGTransform repo.  
AI should be able to help me, if I upload DataLoader module.  
Do data exploration using Pandas, Numpy.  

Try to run model, upload all code to AI, had it explain the different parts.  
Transfer to Jupyter Notebook format.  Run training, then prediction on test samples.  

### Due early Jan 2025  
contract  
timesheet  
***Colab free AI startup, sign up***      

### Jan 2, 2025 notes:    
Need 2-3 full days to test loading data files w PyTorch *.pt format.   

#### Jan 3, 2025 Friday notes:  
Got train.pt and test.pt PTB source files to load in PyTorch. Yeah!!!    
Data are tensors, but no weights, no checkpoints.  
Will need to train the model myself, but author says they used foundational models with pretrained transformer weights.  
Which ine are they talking about?  

Try running Kaggle csv data and random forest w XGBoost library first.  
Probably easiest one to reproduce.  
There is also nn model w Resnet, also using Kaggle csv data.  

After that, try ECGTransform model, along w Resnet using .pt pre-processed files.  

### Jan 9 notes  
Next call Tuesday, too short time to do anything meaningful. OK, just do small follow ups.  
Chinese database link, take a look  
Run Framwork NB Rodrigo provided, as is fist.  
If possible do PTB dataset on 1Dcnn next, but don't stree if no time.  
DO send engagement letter, timesheet.  
May not matter in the end, for various reasons, but good form.  

> Next week, write up initial finding so far, post on datasciY website as project.  






