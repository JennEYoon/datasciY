#"""doc string"""
#---------------------------------------------------------------------
# Author:      Jennifer Yoon
# File, Path:  module1.py, C:\GDrive\Coding\Python
# Start Time:  06/09/2017  18:00
#---------------------------------------------------------------------
import random

def quicksort(xarray, pivot):

    for x in xarray:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return(less, greater)

#  Randomly generate a list of integers.
print("Generate a list of random integers.--------------")
xarray = [random.randint(0, 50) for x in range(10)]
print(xarray, "length ", len(xarray))
pivot = xarray[int(len(xarray)/2)]
print("pivot number from middle of list is ", pivot)

#  First call to split original array into less and greater lists.
print("First gen call to split list. --------------------")
less, greater = [], []
quicksort(xarray, pivot)
print(less, greater, "pivot", pivot)
xarray2 = less
xarray3 = greater

# Second call less-half.
print("Second gen left-half call to re-split list.---------")
pivot2 = xarray2[int(len(xarray2)/2)-1]
less, greater = [], []
quicksort(xarray2, pivot2)
print(less, greater, "pivot", pivot2)

xarray4 = less
xarray5 = greater

# Second call greater-half.
print("Second gen right-half call to re-split list.-------")
pivot3 = xarray3[int(len(xarray3)/2)]
less, greater = [], []
quicksort(xarray3, pivot3)
print(less, greater, "pivot", pivot3)

xarray6 = less
xarray7 = greater

# Tree-binary calls there after.
less, greater = [], []
