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

#### Main links to Xarray tutorial  

https://github.com/xarray-contrib/xarray-tutorial   
https://github.com/xarray-contrib/xarray-tutorial/tree/master/scipy-tutorial  

#### notebooks links, copied to my CoLab account, google drive.  

0:  https://colab.research.google.com/drive/1kTIT_VbvQWdQZgvm3m9bd3HGRQFqR4vZ#scrollTo=mQajzprSBiui 

1:  https://colab.research.google.com/drive/1FEDCL_THbJmpxaFq7LHx1loBwSqeynpB  

2:  https://colab.research.google.com/drive/1dnhXsmT10cwGIzhCUnGK-dxynmNKz-6l#scrollTo=OK2KnMYP-1uT  

3:  https://colab.research.google.com/drive/1lw09Ai9G9wHZd5vuvoZafO_Daerd1eY3  

Others:  

#### Examples  

Geo-Spatial data collected on AWS Open data:
https://hub.aws-uswest2-binder.pangeo.io/user/pangeo-data-lan-utorial-gallery-b6rs8qe9/lab?autodecode  
