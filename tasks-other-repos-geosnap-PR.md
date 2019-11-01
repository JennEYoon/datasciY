# My Task Notes for other Repos.  

#### To merge updates, geosnap repo - done 10/5/2019 Saturday.    
     
   Contribute to Source Repo, Pull Request from MyFork repo.  
     - Open Bash, cd to folder, create new-branch, commit changes to new-branch, push changes to MyFork.  
     - ```git branch <NEW-BRANCH>, git checkout <NEW-BRANCH>```
     - ```git add . , git commit -m "message" ```
     - ```git push origin <NEW-BRANCH>```  
     - May also need to create New-Branch from online Github, on MyFork repo.
     - From online Github, button-prompt to create a Pull Request.  
  
     * May need to squash commits into one commit. May need to name new-branch with "issue-number". 
       Follow maintainer's instructions.  

---------------------------------------------------  
#### Hactoberfest 2019 Progress.  

https://hacktoberfest.digitalocean.com/profile  
Will pass review period on 10/31/2019 4:00 AM.  
Probably won't get T-shirt.  150,000 signed up, more than 50,000 finish before me.  

#### geosnap repo - volunteer to contribute

 - review code, finish fix and PR.
 - Later install and try out software.  
 ----------------  
 - Part of University of California Riverside.  
 - Part of PySal, a large python spatial analysis package.  
 
####  Hactoberfest, for repo for easy commit.  
 - Finish by Tuesday 10/14/2019.  
 - Submitted 2 PR to my own SECdatapy - good. 
 - 1 PR to Hactoberfest2019 - bad, not qualify; later changed did qualify. 
 - Do 2 PR to WCC Getting Started WSL branch. done 10/25/2019 Janelia Fall Fair.  
 - **Finish GeoSmap PR by tomorrow, 10/24/2019 TH -- Big One.**  
   * Started reading description and source doe.  
   * two parts, first one seems doable.  
   * 10/25 Friday, ~4 h, read through source code, instructions again.
   * 10/28 Monday - ~1h read instructions again, notebooks browse. 
     - After Zoysia, 1.5h planted/dug 1st sheet.  
   * 10/29 Tuesday - 1h review, 2h Zoysia 2 more sheets.  
   * 10/30 Wednesday - 1h review, I think I finially figured out what needs to be done.  
     Really, Really need to finish today!  After 2-3h Zoysia.  
   
   **Really need to finish GeoSnap PR.  10/28/2019 M.**  
     - Do #1 today.  
     - Finish #2 tomorrow. 
     - Do PR Tuesday or Wednesday.  
     **Really, Really need to finish today, Wednesday 10/30.**  
     I think I finally understand what I need to do to finish both parts.  
     - 10/31 Really need to finish today.  I go to Mrs Lee for hair in AM.  
       Copy files to review while there.
      * Finished Hactoberfest 4 AM 10/31/2019, 7 day review period ends -- qualitifed for T-shirt.
        Order filled out.  Women's XL heathered Navy color, with purple logo.  
        Still within 50,000 - even though my last PR was 10/24 3 AM!  :-) Great!
     
   https://github.com/spatialucr/geosnap/issues/59  
     Volunteer commit 10/5/2019 - Saturday 9pm.   
     instructions **received 10/7/2019 - Monday** afternoon  
     21 days ago!  
     
     
### >awesome, thanks @JennEYoon! we dont have a contributor guide yet, thanks for raising that.  

#### Here are the details on this issue:

we have a function that converts currency variables for inflation. When a user stores a longitudinal dataset like LTDB or NCDB in geosnap's database, the function that reads in the data sends the appropriate columns to the inflation adjuster function. Here is what that looks like for the LTDB reader. Notice that the **columns in the list** match the currency variables in the **ltdb column of variables.csv**. What still needs to be done are two things:

1. verify that the **columns in inflate_cols on line 494** are all the currency variables in **LTDB**. This would mean going through each of the rows of **variables.csv** and looking for those variables that represent currency of some kind and making sure **each one is listed in inflate_cols**.  

  * function in data/data.py, inflate_cols (line 494 - 509)  
  * LTDB column name in variables.csv -- look for currency of some kind, any missing from function defintion list?  

2. copy logic similar to **lines 494-509** into the **store_ncdb function**, but making sure that the **inflate_cols** in this case match the currency variables from the **ncdb column in variables.csv**.  

  * function in data/data.py, copy inflate_cols function into "store_ncdb" function definition.  
  * Match definition list to NCDB column, currency of some kind, in variables.csv.  

Example notebooks: https://github.com/spatialucr/geosnap/tree/master/examples  

geosnap has 4 modules: data, analyze, harmonize, visualize  

Install instructions:  
cd into cloned repo local.

conda env create -f environment.yml
conda activate geosnap 
python setup.py develop

#### Update 10/31/2019 9:50 PM  

Finally finished PR for geosnap data.py.  Really difficult to figure out what is going on, even though it is a very simple Python file.  Had to read the instructions many, many times.  Sample was good for really getting what is going on.  There is no "currency exhange" involved.  Only USD Deflator and inflation adjustment in US dollars.  Very confusing because eli kept saying "add missing currency."  

Got T-Shirt,  Finished before 10/31/2019 midnight, so will have another +1 bonus PR. 



--- end --- 
 
     
