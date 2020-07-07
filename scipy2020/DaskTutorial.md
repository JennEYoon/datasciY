# Dask Tutorial - Tuesday morning  

Similar to numpy, but for large data sets or processes that can be parallelized.

Xarray uses Dask under the hood.  Is higher level.
Dask allows you to use it in high-level, where processes are set for you, or lower level, where you specify optimal processes. 
Chunk size has optimal range, not too large (just running Numpy) or too small (too much function call overhead). 

For reference, here are the Dask array best practices docs https://docs.dask.org/en/latest/array-best-practices.html
