# Add binder demo to projects

Link to Github: notebooks repo for testing mybinder.org hosting.  
https://github.com/JennEYoon/notebooks

Link to environment.yml file created.  
https://github.com/JennEYoon/notebooks/blob/master/environment.yml

Link to mybinder.org example.ipynb file on mybonder
https://mybinder.org/v2/gh/JennEYoon/notebooks/master?filepath=example.ipynb  
-- takes long time to rebuild instance.  

# Open in CoLab with badge  

Using Google Colab with GitHub
Google Colaboratory is designed to integrate cleanly with GitHub, allowing both loading notebooks from github and saving notebooks to github.

Loading Public Notebooks Directly from GitHub
Colab can load public github notebooks directly, with no required authorization step.

For example, consider the notebook at this address: https://github.com/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb.

The direct colab link to this notebook is: https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb.

To generate such links in one click, you can use the Open in Colab Chrome extension.

Browsing GitHub Repositories from Colab
Colab also supports special URLs that link directly to a GitHub browser for any user/organization, repository, or branch. For example:

http://colab.research.google.com/github will give you a general github browser, where you can search for any github organization or username.
http://colab.research.google.com/github/googlecolab/ will open the repository browser for the googlecolab organization. Replace googlecolab with any other github org or user to see their repositories.
http://colab.research.google.com/github/googlecolab/colabtools/ will let you browse the main branch of the colabtools repository within the googlecolab organization. Substitute any user/org and repository to see its contents.
http://colab.research.google.com/github/googlecolab/colabtools/blob/master will let you browse master branch of the colabtools repository within the googlecolab organization. (don't forget the blob here!) You can specify any valid branch for any valid repository.
Loading Private Notebooks
Loading a notebook from a private GitHub repository is possible, but requires an additional step to allow Colab to access your files. Do the following:

Navigate to http://colab.research.google.com/github.
Click the "Include Private Repos" checkbox.
In the popup window, sign-in to your Github account and authorize Colab to read the private files.
Your private repositories and notebooks will now be available via the github navigation pane.
Saving Notebooks To GitHub or Drive
Any time you open a GitHub hosted notebook in Colab, it opens a new editable view of the notebook. You can run and modify the notebook without worrying about overwriting the source.

If you would like to save your changes from within Colab, you can use the File menu to save the modified notebook either to Google Drive or back to GitHub. Choose File→Save a copy in Drive or File→Save a copy to GitHub and follow the resulting prompts. To save a Colab notebook to GitHub requires giving Colab permission to push the commit to your repository.

Open In Colab Badge
Anybody can open a copy of any github-hosted notebook within Colab. To make it easier to give people access to live views of GitHub-hosted notebooks, colab provides a shields.io-style badge, which appears as follows:

Open In Colab

The markdown for the above badge is the following:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
The HTML equivalent is:

<a href="https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>
Remember to replace the notebook URL in this template with the notebook you want to link to.

----------  



Blub about Matplotlib 3D plotting examples and MyBinder.org.  
Number of instances and memory are limited, not guranteed uptime.  When demo with 30 people simultaneously accesing binder, does not work well, latency.  Have backup of CoLab.  Users use own account to log into Google Cloud resources, not limited, can handle more.  Save locally first, then upload to Github in a new commit.

# Update links from PyDataNY -- tutorials, use video link and pdf if available.  
Testing tutorial: Stanley van der Merwe, Petr Wolf: From Raw Recruit Scripts to Perfect Python | PyData New York 2019
Youtube video link: https://www.youtube.com/watch?v=vqLfJbo-vOs  
