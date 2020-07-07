# Dask Tutorial - Tuesday morning  

Similar to numpy, but for large data sets or processes that can be parallelized.

Xarray uses Dask under the hood.  Is higher level.
Dask allows you to use it in high-level, where processes are set for you, or lower level, where you specify optimal processes. 
Chunk size has optimal range, not too large (just running Numpy) or too small (too much function call overhead). 

When to use Zarr?  
  * hdf5 is a file format, fixes csv format data problem for large files. 
  * Zarr keeps meta data in separate file and chunks into smaller pieces. Cloud friendly. hdf5 reads full file only.  can't be donwloaded in chunks from cloud.

For reference, here are the Dask array best practices docs https://docs.dask.org/en/latest/array-best-practices.html

### sort does not work well in parallel.  

### Development is done by volunteers who work on different companies. Only develop what the companies are interested in.  Can't depend on development.  

Dask Arry is like numpy  

Dask DataFrame is like pandas  
