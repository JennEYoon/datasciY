# PySAL Friday 

Data sources:  
https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
https://github.com/spatialucr/geosnap 
SciPy Logistics Eli says: @Dan check out https://github.com/cenpy-devs/cenpy
for r it's tidycensus 

I have a workflow that uses a clipping operation, where I use geopandas .geometry.unary_union + geometry.intersects and it is extremely slow. I haven't tried using gdal directly from command line (which I've seen recommended). Any tips from folks about clipping and speeding up performance? (if this will be covered in later notebook, i can wait :) )
eli if you have the most recent geopandas (>=0.8) you could try install pygeos
eli (pygeos will speed up your spatial operations significantly)
eli and as long as it's installed, geopandas will use it automatically

Solutions: 
scag.geoid.str[:5].unique()

This works for me, using groupby:
scag["county"] = scag.geoid.str[:5]
for fips, county in scag.groupby("county"):
county.to_file(f"data/{fips}.shp")

### Notebook 1 - visualize quick & dirty inside PySAL  
 Partner with desktop GIS, so can use 
 
 Map Classifier
 
 what was .adcm?
a few seconds ago
Zafer
Absolute deviation around class median (ADCM)

you'd use a UserDefined class
a minute ago
eli
with UserDefined https://pysal.org/mapclassify/generated/mapclassify.UserDefined.html#mapclassify.UserDefinedyou pass a set of bins, and you can use the resulting labels to create a map 

TES
89m 48s
In future , is there any plan to include some statistical analysis of raster data in Pysal as there are libraries such as rasterstats which generate stats but very slow for huge geometries and not powerful as PySal in terms of analysis.
Shubham
eli its under development at the moment :)
Shubham Really looking forward to it....any library can you suggest which is good for raster statistical analysis ?
eli https://github.com/perrygeo/python-rasterstats
eli https://github.com/mapbox/rasterio
eli https://github.com/makepath/xarray-spatial



