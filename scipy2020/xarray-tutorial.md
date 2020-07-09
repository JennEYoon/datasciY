# Xarray Tutorial - Thursday morning.

Kelvin -- we'll get into xarray.Dataset shortly, which has the equivalent of multiple columns

dimension is refers to length of coordinates and coordinates themselves are labels to data point. is this how I should understand these?

How can there be 2 different coordinates for 1 dimension?
Andrew J
Ryan Abernathey We distinguish between a "dimension coordinate", which is used for indexing, and a "non dimension coordinate" which is not. You can have as many non-dimension coordinates as you want.
Ryan Abernathey But only one dimension coordinate per dimension
Ryan Abernathey http://xarray.pydata.org/en/stable/data-structures.html#coordinates

>https://mybinder.readthedocs.io/en/latest/user-guidelines.html
>mybinder.org Usage Guidelines — Binder 0.1b documentationmybinder.readthedocs.io › latest › user-guidelines
>Maximum Concurrent Users for a Repository We don't want a single repository to dominate all of the traffic to Binder, so we've set a maximum limit of concurrent user >sessions that point to the same Binder link. The maximum number of simultaneous users for a given repo is 100.
>
>Open in CoLab, then save a copy to Google Drive, works a lot better.  

sel select, uses pandas under the hood.
XArray benefit over Pandas, is multiple index names, not limited to column name and column index number.  
Cordinate-Dimension (same name) allows to call item and get value using the same name?  
isel index select, same as numpy to select based on index number

110m 18s
Time when question was addressed
When you have a chance, maybe during next break, can you go over the main selling point of XArray again? Crowdsource bumped me into Python tutorial while I was waiting, and I didn't realize it until 20 minutes into this tutorial. :-(  
  * Stephan Hoyer Xarray is useful for adding generic labels like dimension names and coordinates to your NumPy arrays  
  * Metadata, labeling.  Sits on top of numpy, pandas - for calculations, matplotlib, bokeh (hvplot syntax) - for plotting 
    Dask for parallelism.  Mostly reads from data files in various formats, hdf5, it's own format... 
    Specify chunks in 512x512 minimum tile size AWS. Usually around 100 MB size.  
  * Plotting - initial pass use xarray for convenient features (auto-labelling axis, labels, colorbar), then use matplotlib for customization. 
    ax = ax, then set each item.  Pass-through all of matplotlib methods.  

Is it possible to compute quantiles?
Kenneth
Joe Hamman yes! datasets and dataarrays both have a `quantile` method: http://xarray.pydata.org/en/stable/generated/xarray.Dataset.quantile.html#xarray.Dataset.quantile


#### Main links to Xarray tutorial  

https://github.com/xarray-contrib/xarray-tutorial   
https://github.com/xarray-contrib/xarray-tutorial/tree/master/scipy-tutorial  
PyData organization:  http://xarray.pydata.org/en/stable/generated/...  

#### notebooks links, copied to my CoLab account, google drive.  

0:  https://colab.research.google.com/drive/1kTIT_VbvQWdQZgvm3m9bd3HGRQFqR4vZ#scrollTo=mQajzprSBiui 

1:  https://colab.research.google.com/drive/1FEDCL_THbJmpxaFq7LHx1loBwSqeynpB  

2:  https://colab.research.google.com/drive/1dnhXsmT10cwGIzhCUnGK-dxynmNKz-6l#scrollTo=OK2KnMYP-1uT  

3:  https://colab.research.google.com/drive/1lw09Ai9G9wHZd5vuvoZafO_Daerd1eY3  

4: https://colab.research.google.com/drive/1TzfY7NNqltpkW92UmJDd0Um4-QZciIbV#scrollTo=BKG8dsMm_HXX  

Others:  
More resources - Plotting (notebook 4): 
Xarray's visualization gallery: https://xarray.pydata.org/en/stable/examples/visualization_gallery.html
Xarray's plotting documentation: https://xarray.pydata.org/en/stable/plotting.html
hvplot's plotting documentation: https://hvplot.holoviz.org/user_guide/Gridded_Data.html  
  Interactive plotting, move cursor to get data points on chart, similar to plotly.  

#### Examples  

Geo-Spatial data collected on AWS Open data:
https://hub.aws-uswest2-binder.pangeo.io/user/pangeo-data-lan-utorial-gallery-b6rs8qe9/lab?autodecode  



