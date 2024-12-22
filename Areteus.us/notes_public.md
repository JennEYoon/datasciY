# Notes on Areteus project, public here  
Private notes in Jennifer-Yoon private repo.  

### Dec 22, 2024 Sunday notes:  

 * Find Colab pricing, $10/month pro?  Better GPU?  
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




