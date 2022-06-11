# Do a demo of MatPlotLib library uses.  

Projects.html root page.  
Short blurb, followed by notebook link, public, uploaded to AWS.   
Ref to "Anatomy of matplotlib" tutorial, SciPy 2018.  
Get notebook source from Github.  

Standardize methods for all plots, use ax method, OOM  
Brief discussion of Pyplot method, for use in shells, not notebook.  
Set backend to interactive, ion off.  
```
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
```  

#### OO method explicitly call method on ax objects.  
```
x = np.linspace(0, 2, 100)

# Note that even in the OO-style, we use `.pyplot.figure` to create the figure.
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(x, x, label='linear')  # Plot some data on the axes.
ax.plot(x, x**2, label='quadratic')  # Plot more data on the axes...
ax.plot(x, x**3, label='cubic')  # ... and some more.
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()  # Add a legend.
```  

Backtick on iPad, .?123 key, ' key hold, options appear for backtick, flick.  

#### or (pyplot-style)
```
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```  

Main defference, OO style uses ax.something, while pyplot style uses plt.something.  
Both styles create figure same way, <code>fig, ax = plt.subplots() </code>  
or ```figure = plt.figure()```


Passing data as a dictionary-like object, read from Excel Spreadsheet.  
Passing data defined in a math function.  

Graph and bars and tickmarks for stdev, mean. 

Graph with red bars for negative loss values.  

Graph with fill region for +/- stdev.  
Forecast graph with filled regions.  

Image 

Geospatial scatter plot, mark size depend and number of cases.  
