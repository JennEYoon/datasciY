# My Task Notes for other Repos.  

#### To merge updates, geosnap repo - done 10/5/2019 Saturday.  
  1. Fork on my account Github  
     - Log into my account Github, go to source github repo, click button to "Fork."  
  2. Create git repo locally on my computer     
     - Start Bash, cd to new folder, 
     - ```git init, git clone <MYFORK-URL.git>```  
     - Add remote upstream 
     - ```git remote add upstream <SOURCE-URL.git>```  
     * End up with two remotes, origin (MYFORK), upstream (SOURCE).  
  
  3. Sync changes from Source Repo, push to MyFork repo.  
     - ```git pull upstream <MASTER>, git push origin <MASTER>```  
     
  4. Contribute to Source Repo, Pull Request from MyFork repo.  
     - Open Bash, cd to folder, create new-branch, commit changes to new-branch, push changes to MyFork.  
     - ```git branch <NEW-BRANCH>, git checkout <NEW-BRANCH>```
     - ```git add . , git commit -m "message" ```
     - ```git push origin <NEW-BRANCH>```  
     - May also need to create New-Branch from online Github, on MyFork repo.
     - From online Github, button-prompt to create a Pull Request.  
  
     * May need to squash commits into one commit. May need to name new-branch with "issue-number". 
       Follow maintainer's instructions.  
       
#### My notes on [Git-Fork-Branch](wip1/udacity-github/Git-Fork-Branch-memo.txt).  

---------------------------------------------------  

#### dlaicourse repo - from LMoroney - Don't Merge.     
 - Different TensorFlow class on Coursera.  

#### geosnap repo - volunteer to contribute, but commented a question.  
 - Later install and try out software.  
 - Part of University of California Riverside.  
 - Part of PySal, a large python spatial analysis package.  
   
#### inequality repo - small package, related to geosnap? Only lossly. 
 - Part of PySal package.  
 - Next week try it out along with geosnap.  
 
 