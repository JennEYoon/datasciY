# Do a demo of MatPlotLib library uses.  

Projects.html root page.  
Short blurb, followed by notebook link, public, uploaded to AWS.   
Ref to "Anatomy of matplotlib" tutorial, SciPy 2018.  
Get notebook source from Github.  

Standardize methods for all plots, use ax method, OOM  
Brief discussion of Pyplot method, for use in shells, not notebook.  
Set backend to interactive, ion off.  

fig, ax = plt.subplots()  with s.  
ax.set ...  

fig = plt.figure()  
ax = plt.add_subplot() no s.  

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes

Both pyplot method and OOP method start off the same way to create a figure object.  
The easiest way to create a new figure is with pyplot:

fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

Passing data as a dictionary-like object, read from Excel Spreadsheet.  
Passing data defined in a math function.  

Graph and bars and tickmarks for stdev, mean. 

Graph with red bars for negative loss values.  

Graph with fill region for +/- stdev.  
Forecast graph with filled regions.  

Image 

Geospatial scatter plot, mark size depend and number of cases.  
