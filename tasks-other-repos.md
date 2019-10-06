# My Task Notes for other Repos.  

* To merge updates, geosnap repo - done 10/5/2019 Saturday.  
  1. Fork on my account Github 
     - Log into my account Github, go to source github repo, click button to "Fork."
  2. Create git repo locally on my computer     
     - Start Bash, cd to new folder, git init, "git clone <MYFORK-URL.git>"  
     - Add remote upstream "git remote add upstream <SOURCE-URL.git>"  
     * End up with two remotes, origin (MYFORK), upstream (SOURCE).
  
  3. Sync changes from Source Repo, push to MyFork repo.  
     - git pull upstream <master>  
     - git push origin <master>
     
  4. Contribute to Original Repo, Pull Request from MyFork repo.
     - Open Bash, cd to folder, crate new-branch, commit changes to new-branch, push to MyFork.  
     - "git branch <new-branch>", "git checkout <new-branch>"
     - "git push origin <new-branch>"     
     - From online Github, button-prompt to create a Pull Request.  
     * May need to squash commits into one commit.  May need to name new-branch with "issue#num".  Follow maintainer's instructions.  
  
  My notes on [Git-Fork-Branch](wip1/udacity-github/Git-Fork-Branch-memo.txt).  

* Don't Merge - dlaicourse repo from LMoroney.  Different TensorFlow class on Coursera.  

* geosnap repo - volunteer to contribute, but commented a question.  Later install and try out software.  
   Part of University of California Riverside.  Part of PySal, a large python spatial analysis package. 
   
* inequality repo - small package, related to geosnap?  Part of PySal package.  
