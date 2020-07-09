# Xarray Tutorial - Thursday morning.

All 3 speakers has Oceanography and Atmospheric jobs.
Must be useful for plotting, using Dask to parallelize tasks.  

---  

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

graph not showing on notebook 4:  pyviz jupyter lab extension fixed the problem btw  
" Should just work in binder "  

---  

#### Main links to Xarray tutorial  

https://github.com/xarray-contrib/xarray-tutorial   
https://github.com/xarray-contrib/xarray-tutorial/tree/master/scipy-tutorial  
PyData organization:  http://xarray.pydata.org/en/stable/generated/...  
   https://github.com/pydata/xarray/  

#### References
Documentation  http://xarray.pydata.org/en/stable/  
Code Repository  https://github.com/pydata/xarray  
Ask for help:
Use the python-xarray on StackOverflow  https://stackoverflow.com/questions/tagged/python-xarray  
GitHub Issues for bug reports and feature requests  https://github.com/pydata/xarray/issues  

#### notebooks links, copied to my CoLab account, google drive.  

0:  https://colab.research.google.com/drive/1kTIT_VbvQWdQZgvm3m9bd3HGRQFqR4vZ#scrollTo=mQajzprSBiui 

1:  https://colab.research.google.com/drive/1FEDCL_THbJmpxaFq7LHx1loBwSqeynpB  

2:  https://colab.research.google.com/drive/1dnhXsmT10cwGIzhCUnGK-dxynmNKz-6l#scrollTo=OK2KnMYP-1uT  

3:  https://colab.research.google.com/drive/1lw09Ai9G9wHZd5vuvoZafO_Daerd1eY3  

4: https://colab.research.google.com/drive/1TzfY7NNqltpkW92UmJDd0Um4-QZciIbV#scrollTo=BKG8dsMm_HXX  

5:  https://colab.research.google.com/drive/1nFnwHBFIgsbchJv7NsH-ALREIcV0BgmM  

6:  https://colab.research.google.com/drive/1oMUHalabWJhkyZCpKVnX-RXwLuWUuah_  

Others:  
More resources - Plotting (notebook 4): 
Xarray's visualization gallery: https://xarray.pydata.org/en/stable/examples/visualization_gallery.html
Xarray's plotting documentation: https://xarray.pydata.org/en/stable/plotting.html
hvplot's plotting documentation: https://hvplot.holoviz.org/user_guide/Gridded_Data.html  
  Interactive plotting, move cursor to get data points on chart, similar to plotly.  

#### Examples  



## Going Deeper

We've designed the notebooks above to cover the basics of Xarray from beginning
to end. To help you go deeper, we've also create a list of notebooks that
demonstrate real-world applications of Xarray in a variety of use cases. These
need not be explored in any particular sequence, instead they are meant to
provide a sampling of what Xarray can be used for.

### Xarray and Weather/Climate Model Data

1. [Global Mean Surface Temperature from CMIP6](https://binder.pangeo.io/v2/gh/pangeo-gallery/cmip6/binder?urlpath=git-pull?repo=https://github.com/pangeo-gallery/cmip6%26amp%3Burlpath=lab/tree/cmip6):
   Start with `global_mean_surface_temp.ipynb` then feel free to explore the
   rest of the notebooks.
   <!-- 1. [Natural climate variability in the CESM Large Ensemble](https://aws-uswest2-binder.pangeo.io/v2/gh/NCAR/cesm-lens-aws/master?urlpath=lab) -->
1. [National Water Model Streamflow Analysis](https://aws-uswest2-binder.pangeo.io/v2/gh/rsignell-usgs/esip-gallery/binder?urlpath=git-pull?repo=https://github.com/rsignell-usgs/esip-gallery%26amp%3Burlpath=lab/tree/esip-gallery):
   Start with `02_National_Water_Model.ipynb` then feel free to explore the rest
   of the notebooks.  
   
### Xarray and Satellite Data

1. [Landsat-8 on AWS](https://aws-uswest2-binder.pangeo.io/v2/gh/pangeo-data/landsat-8-tutorial-gallery/master/?urlpath=git-pull?repo=https://github.com/pangeo-data/landsat-8-tutorial-gallery%26amp%3Burlpath=lab/tree/landsat-8-tutorial-gallery/landsat8.ipynb%3Fautodecode)

(me) * Geo-Spatial data collected on AWS Open data:
https://hub.aws-uswest2-binder.pangeo.io/user/pangeo-data-lan-utorial-gallery-b6rs8qe9/lab?autodecode   

### Xarray and Baysian Statistical Modeling

1. [Xarray and PyMC3](https://mybinder.org/v2/gh/pymc-devs/pymc3/master?filepath=%2Fdocs%2Fsource%2Fnotebooks):
   Start with `multilevel_modeling.ipynb` then feel free to explore the rest of
   the notebooks. Also checkout [Arviz](https://arviz-devs.github.io/arviz/)
   which uses Xarray as its data model. 



