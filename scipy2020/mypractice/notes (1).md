Probability vs likelihood

likelihood the math function to evaluate data against model.
probability the tendendy to generate an outcome that we observe. 

Mike Betancourt has an elegant Introduction to Probability Theory (For Scientists and Engineers) 

Jake Vanderplas Statistics for Hackers 2015 talk. 

Binder use every 10 minutes, else memory goes away. 

Very good example:
https://github.com/justinbois/bokeh-catplot
https://github.com/justinbois/dataframed-plot-examples 
http://bois.caltech.edu/dist_stories/t3b_probability_stories.html

Blog post again: http://allendowney.blogspot.com/2013/08/are-my-data-normal.html 

All the ECDF shows us is that there is no evidence that the data do not follow the model. Absence of evidence is not evidence of absence. 

for those who search alternative choices (instead of Poisson) for football goals. (further reading https://www.sciencedirect.com/science/article/pii/S0378437102010300 ) 

Inst: porisson only describes the mean, no width/distribution. Move to negative binomial if you want both.  

https://carlzimmer.com/books/science-ink-tattoos-of-the-science-obsessed/

(Note that KL divergence is an asymmetric measure)
So cross-entropy as a measure of the average number of additional bits needed to encode your data by the model

relationship between distributions! 
Full chart at http://www.math.wm.edu/~leemis/2008amstat.pdf
https://www.johndcook.com/blog/distribution_chart/

Tip for binder users. Create a new notebook. Run this in the first cell:
from time import sleep
# continuous runner
while True:
print(".", sep='')
sleep(120)

Apple Notes on iPad, cast to crowdcast video.

Notebook 2: Parameter est & hypothesis testing.  

https://carlzimmer.com/books/science-ink-tattoos-of-the-science-obsessed/

For books, I might recommend Osvaldo Martin's book: https://www.amazon.com/Bayesian-Analysis-Python-Introduction-probabilistic-ebook/dp/B07HHBCR9G

There's also going to be a sequel to Osvaldo's book that is going into more depth coming out Feb 2021: https://docs.google.com/forms/d/e/1FAIpQLSeGA_6AZIIat6vSds9pOEao0VN_svijqafEDOWo-Rxt38ljmw/viewform

Jeffrey's prior, flat like uniform prior, but interval is smaller. from 1/1-p instead of over 0 to 1.  Posterior transforms into U shape, low around middle (p mean).  

MCMC link
https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50

I conda installed pymc3, and it seemed to complete successfully. But Notebook crashes wen I run it on import pymc3 as pm

same happened to me, this fixed it https://stackoverflow.com/questions/42014710/python-pip-conda-install-pymc3-error

https://twiecki.io/blog/2013/08/27/bayesian-glms-2/

https://pdfs.semanticscholar.org/dea6/0927efbd1f284b4132eae3461ea7ce0fb62a.pdf
http://www.asmfc.org/files/Science/FBmodels.pdf


Basics: Allen Downey last year 
Decision Making: last year tutorial ... 
PyMC4:  to be 
Bayesian analysis recipies: Instructor, will post.  

Lookout for updates to Github tutorial notebooks.  More links to be posted.  