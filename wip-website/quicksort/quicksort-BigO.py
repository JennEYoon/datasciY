#---------------------------------------------------------------------
# Author:      Jennifer Yoon
# File, Path:  module1.py, C:\GDrive\Coding\Python
# Start Time:  06/09/2017  18:00, 6/10 20:00 continue,
# time:        06/11/2017  12:30 pm to 6/12 2 am, 6/12 13:30 continue...
#---------------------------------------------------------------------
import random

xarray = [random.randint(0, 100) for x in range(21)]
orig = xarray[:]
print("L11 random list:", xarray, " length:", len(xarray))
sorted = quicksort(xarray)
print("sorted list:", sorted, " original list:", orig)

def quicksort(xarray):

    # Calculate pivot value.
    index = int(len(xarray)/2)
    pivot = xarray[index]
    xarray.pop(index)

    lesser, greater = [], []
    for x in xarray:
        print("L24 for-if, count 1")
        if x < pivot:
            lesser.append(x)
        else:
            greater.append(x)

    left, mid, right = lesser, [pivot], greater
    if len(left) > 1 and len(right) > 1:
        print("L31 if, call left, call right, Count 3.")
        return(quicksort(left) + mid + quicksort(right))
    elif len(left) >1:
        print("L34, if2, call left, Count 3.")
        return(quicksort(left) + mid + right)
    elif len(right) > 1:
        print("L37, if3, call right, Count 4.")
        return(left + mid + quicksort(right))
    else:
        print("L40 3ifs, no calls, Count 3.")
        return(left + mid + right)


""" notes:
0) create random list.
1) pick middle pivot, index, value.
2) full list -- compare with pivot value, attach to left or right.
3) reassemble left + pivot + right, return up the tree.
4) left section, recursive call
5) right section, recursive call
6) reassemble sub-array, left + pivot + right.
7) stop if length of sub-section is 0.
8) if length == 1, don't sort, just assemble.

##xarray = [6, 14, 4, 20, 10, 19, 15, 5, 11]
##xarray = [6, 4, 21, 20, 10, 19, 15, 5, 3]
##xarray = [6, 8, 21, 7, 14, 20, 10, 19, 15, 5, 3, 9, 12]
"""